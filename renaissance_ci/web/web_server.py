from flask import Flask, render_template
import asyncio
import concurrent.futures
import renaissance_ci.core.chain
import renaissance_ci.core.chainLinksDocker
import renaissance_ci.core.ChainGenerator as ChainGenerator

app = Flask(__name__)
app.template_folder = '../resources/templates'
loop = asyncio.get_event_loop()
executor = concurrent.futures.ThreadPoolExecutor(max_workers=3,)


@app.route('/')
def test_template():
    return render_template("home.html",
                           name="billy",
                           result=renaissance_ci.core.chain.PipelineChainLink.__subclasses__())


@app.route('/chain')
def test_chain():
    chain = ChainGenerator.generate_docker_chain_link()
    loop.run_in_executor(executor, start_chain, chain)
    return "ok"


def start_chain(chain):
    chain.run()
    print("chain completed")


if __name__ == '__main__':
    app.run()
