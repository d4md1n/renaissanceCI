from renaissance_ci.core.chain import PipelineChainLink

import docker
import os


class SayHelloFromDocker(PipelineChainLink):
    def before_process(self):
        self.client = docker.APIClient(base_url='unix://var/run/docker.sock')

    def process(self):
        container = self.client.create_container(
            image='alpine:latest',
            command="echo hello world",
            working_dir="/home"
        )
        self.client.start(container)
        self.result = container.get("Id")
        self.client.wait(container)
        print(self.client.logs(container))

    def after_process(self):
        print(self.result)


class GitCheckoutFromDocker(PipelineChainLink):
    def __init__(self, successor=None, git_repository=''):
        super().__init__(successor)
        self._git_repository = git_repository

    def before_process(self):
        self.client = docker.APIClient(base_url='unix://var/run/docker.sock')
        self.data['host_volume_path'] = os.path.abspath("./test_docker_dir")

    def process(self):
        volumes = ['/home']
        host_volume_path = self.data['host_volume_path']
        volume_bindings = {
            host_volume_path: {
                'bind': '/home',
                'mode': 'rw',
            }
        }

        host_config = self.client.create_host_config(binds=volume_bindings)

        container = self.client.create_container(
            image='governmentpaas/git-ssh:latest',
            command="git clone %s /home" % self._git_repository,
            volumes=volumes,
            host_config=host_config,
        )
        self.client.start(container)
        self.result = container.get("Id")
        self.client.wait(container)
        print(self.client.logs(container))

    def after_process(self):
        print(self.result)


class JavaBuildWithDocker(PipelineChainLink):
    def __init__(self, successor=None, gradlew_command = "build"):
        super().__init__(successor)
        self._gradle_command = gradlew_command


    def before_process(self):
        self.client = docker.APIClient(base_url='unix://var/run/docker.sock')
        self.data['host_volume_path'] = os.path.abspath("./test_docker_dir")

    def process(self):
        volumes = ['/home']
        host_volume_path = self.data['host_volume_path']
        volume_bindings = {
            host_volume_path: {
                'bind': '/home',
                'mode': 'rw',
            }
        }

        host_config = self.client.create_host_config(binds=volume_bindings)


        container = self.client.create_container(
            image='library/java',
            command=("/bin/bash /home/complete/gradlew %s" % self._gradle_command),
            volumes=volumes,
            host_config=host_config, working_dir="/home"
        )
        self.client.start(container)
        self.result = container.get("Id")
        self.client.wait(container)
        print(self.client.logs(container))

    def after_process(self):
        print(self.result)


class ClearDirectoryWithDocker(PipelineChainLink):
    def before_process(self):
        self.client = docker.APIClient(base_url='unix://var/run/docker.sock')
        self.data['host_volume_path'] = os.path.abspath("./test_docker_dir")

    def process(self):
        volumes = ['/home']
        host_volume_path = self.data['host_volume_path']
        volume_bindings = {
            host_volume_path: {
                'bind': '/home',
                'mode': 'rw',
            }
        }

        host_config = self.client.create_host_config(binds=volume_bindings)

        container = self.client.create_container(
            image='alpine:latest',
            command="rm -rf /home",
            volumes=volumes,
            host_config=host_config, working_dir="/home"
        )
        self.client.start(container)
        self.result = container.get("Id")
        self.client.wait(container)
        print(self.client.logs(container))

    def after_process(self):
        print(self.result)