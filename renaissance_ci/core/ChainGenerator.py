from renaissance_ci.core.chainLinksDocker import *


def generate_docker_chain_link():
    clear_directory_with_docker = ClearDirectoryWithDocker()
    java_build_with_docker = JavaBuildWithDocker(clear_directory_with_docker)
    gitCheckoutFromDocker = GitCheckoutFromDocker(java_build_with_docker)
    say_hello_from_docker = SayHelloFromDocker(gitCheckoutFromDocker)
    return say_hello_from_docker


def generate_docker_chain_with_parameters(gitRepo = '', gradle_command = 'build'):
    clear_directory_with_docker = ClearDirectoryWithDocker()
    java_build_with_docker = JavaBuildWithDocker(clear_directory_with_docker, gradle_command)
    gitCheckoutFromDocker = GitCheckoutFromDocker(java_build_with_docker, gitRepo)
    say_hello_from_docker = SayHelloFromDocker(gitCheckoutFromDocker)
    return say_hello_from_docker
