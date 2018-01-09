from flask import Flask, render_template, request
import asyncio
import concurrent.futures
import renaissance_ci.core.chain
import renaissance_ci.core.chainLinksDocker
import renaissance_ci.core.ChainGenerator as ChainGenerator

app = Flask(__name__)
app.template_folder = '../resources/templates'
loop = asyncio.get_event_loop()
executor = concurrent.futures.ThreadPoolExecutor(max_workers=3, )


@app.route('/')
def test_template():
    return render_template("home.html",
                           name="billy",
                           result=renaissance_ci.core.chain.PipelineChainLink.__subclasses__())


@app.route('/chain', methods=['POST'])
def test_chain():
    data = request.form
    print(data)

    chain = ChainGenerator.generate_docker_chain_with_parameters(data['gitRepo'], gradle_command=data['gradleCommand'])
    loop.run_in_executor(executor, start_chain, chain)
    return "chainStarted"


@app.route('/chain/config')
def get_chain_config_page():
    return render_template("chainConfig.html")


def start_chain(chain):
    chain.run()
    print("chain completed")


if __name__ == '__main__':
    app.run()
