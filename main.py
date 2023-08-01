# main.py

import os
import click
import shutil
import re
import json
from jinja2 import Environment, PackageLoader

# Load the configuration from config.json
with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)

# Define a regex pattern for a valid Java class name
CLASS_NAME_REGEX = re.compile(r'^[a-zA-Z_$][a-zA-Z\d_$]*$')

@click.command()
@click.option('--company', prompt='Company name', help='The name of the company')
@click.option('--team-name', prompt='Team name', help='The name of the team')
@click.option('--project-name', prompt='Project name', help='The name of the Spring Boot project')
@click.option('--language', type=click.Choice(['java', 'groovy', 'kotlin']), prompt='Select a programming language', help='Programming language for the project')
@click.option('--java-version', type=click.Choice(config_data['java_versions'].keys()), prompt='Select Java version', default='11', help='Java version for the project')
@click.option('--build-tool', type=click.Choice(['maven', 'gradle']), prompt='Select a build management tool', help='Build management tool for the project')
@click.option('--generate-resources', is_flag=True, prompt='Generate resources and YAML files for all profiles?', help='Generate resources and YAML files for all Spring Boot profiles')
def generate_project(company, team_name, project_name, language, java_version, build_tool, generate_resources):

    package_name = f'com.{company.lower().replace(" ", "")}.{team_name.lower().replace(" ", "")}'

    # Check if the project name is a valid Java class name
    if not is_valid_java_class_name(project_name):
        click.echo('Error: Invalid project name. Please provide a valid Java class name.')
        return

    # Create a new directory for the project
    project_dir = project_name.lower().replace(' ', '_')
    os.makedirs(project_dir, exist_ok=True)

    # Initialize Jinja2 environment
    env = Environment(loader=PackageLoader('main', 'templates'))

    # Create a dictionary of options to pass to the template
    template_vars = {
        'company': company,
        'team_name': team_name,
        'project_name': project_name,
        'package_name': package_name,
        'language': language,
        'java_version': config_data['java_versions'][java_version],
        'build_tool': build_tool,
        'dependencies': [],
        'generate_resources': generate_resources,
    }

    # Prompt user to add dependencies using aliases
    click.echo('Available dependency aliases:')
    for alias, description in config_data['dependency_aliases'].items():
        click.echo(f'  {alias} - {description}')
    click.echo('Type each alias separated by space or type "done" to finish.')

    while True:
        alias_input = input('Enter dependencies using aliases: ')
        if alias_input.lower() == 'done':
            break
        add_dependencies_by_alias(alias_input.split(), template_vars)

    # Generate project files using Jinja2 templates
    generate_files(project_dir, env, template_vars)

    # Create a zip folder for the project
    zip_folder(project_dir)

def is_valid_java_class_name(name):
    return CLASS_NAME_REGEX.match(name) is not None

def add_dependencies_by_alias(aliases, template_vars):
    for alias in aliases:
        if alias in config_data['dependency_aliases']:
            template_vars['dependencies'].extend(config_data['dependency_aliases'][alias])


def generate_files(project_dir, env, template_vars):
    # Create directories
    os.makedirs(os.path.join(project_dir, 'src', 'main', 'java'))
    os.makedirs(os.path.join(project_dir, 'src', 'test', 'java'))

    # Render and save the build tool file (pom.xml or build.gradle)
    build_tool_template = f'{template_vars["build_tool"]}.xml'
    with open(os.path.join(project_dir, 'pom.xml'), 'w') as build_file:
        build_template = env.get_template(build_tool_template)
        build_file.write(build_template.render(**template_vars))

    # Render and save application source file
    main_class = f'{template_vars["project_name"].capitalize()}Application'
    main_file_path = os.path.join(project_dir, 'src', 'main', 'java', f'{template_vars["project_name"]}Application.java')
    with open(main_file_path, 'w') as main_file:
        main_template = env.get_template('Main.java')
        main_file.write(main_template.render(**template_vars, main_class=main_class))

    # Render and save application properties file
    if template_vars['generate_resources']:
        resources_dir = os.path.join(project_dir, 'src', 'main', 'resources')
        os.makedirs(resources_dir)
        with open(os.path.join(resources_dir, 'application.properties'), 'w') as prop_file:
            prop_file.write('spring.profiles.active=default')

        # Generate YAML files for all profiles
        profiles = ['dev', 'prod', 'test', 'stage']  # You can customize this list as needed
        for profile in profiles:
            with open(os.path.join(resources_dir, f'application-{profile}.yml'), 'w') as yml_file:
                yml_template = env.get_template('application.yml')
                yml_file.write(yml_template.render(**template_vars, profile=profile))

def zip_folder(project_dir):
    shutil.make_archive(project_dir, 'zip', project_dir)

# Rest of the code remains the same as in the previous version
if __name__ == '__main__':
    generate_project()
