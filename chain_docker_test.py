from chain import PipelineChainLink

import docker
import os

class SayHelloFromDocker(PipelineChainLink):
    
    def before_process(self):
        self.client = docker.from_env()

    def process(self):
        self.result = self.client.containers.run("ubuntu:latest", "echo hello world")

    def after_process(self):
        print(self.result)

class GitCheckoutFromDocker(PipelineChainLink):
    
    def before_process(self):
        self.client = docker.APIClient(base_url='unix://var/run/docker.sock')
        self.data['host_volume_path'] = os.path.abspath("./test")

    def process(self):
        volumes= ['/home']
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
                                                 command="git clone https://github.com/d4md1n/TrainingApp.git /home",
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
    def before_process(self):
        self.client = docker.APIClient(base_url='unix://var/run/docker.sock')
        self.data['host_volume_path'] = os.path.abspath("./test")

    def process(self):
        volumes= ['/home']
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
                                                 command="/bin/bash /home/gradlew build",
                                                 volumes=volumes,
                                                 host_config=host_config, working_dir = "/home"
                                                ) 
        self.client.start(container)
        self.result = container.get("Id")
        self.client.wait(container)
        print(self.client.logs(container))

    def after_process(self):
        print(self.result)

def main():
    javaBuildWithDocker = JavaBuildWithDocker()
    gitCheckoutFromDocker = GitCheckoutFromDocker(javaBuildWithDocker)
    sayHelloFromDocker = SayHelloFromDocker(gitCheckoutFromDocker)
    sayHelloFromDocker.run()

if __name__ == "__main__":
    main()
