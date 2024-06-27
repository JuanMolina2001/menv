import sys
from os import getcwd
import subprocess
from json import dump, load
cwd = getcwd()

def run():
    scripts = load(open('menv.json','r'))['scripts']
    script = sys.argv[2]
    if script in scripts:
        subprocess.run(scripts[script], cwd=cwd)
    else:
        print(f"script {script} not found")
def save():
    result = subprocess.run(['pip', 'freeze'], capture_output=True, text=True)
    stdout = result.stdout
    requirements= {}
    for r in stdout.replace('==',':').splitlines():
        h = r.split(':')
        requirements.update({h[0]:h[1]})
    f = load(open('menv.json','r'))
    f['requirements'] = requirements
    dump(f,open('menv.json','w'))
def start():
    file =  load(open('menv.json','r'))
    python = file['python']
    if sys.version.split()[0] != python:
        if '--force' not in sys.argv:
            print(f"python version mismatch {sys.version.split()[0]} != {python}")
            return
    requirements = file['requirements']
    packages_to_install = [f"{package}=={version}" for package, version in requirements.items()]
    for package in packages_to_install:
        subprocess.check_call(['pip', 'install', package])
def init():
    args = sys.argv[2:]
    subprocess.run(['virtualenv', 'menv'] + args, cwd=cwd)
    try:
        load(open('menv.json', 'r'))
    except:
        file = open('menv.json','w')
        dump({
            "python":sys.version.split()[0],
            "requirements":{},
            "scripts":{}
            }, file, indent=4)
    
def activate():
    if(sys.platform == 'win32'):
        subprocess.run(f"cmd.exe /K menv\\Scripts\\activate.bat", shell=True)
def deactivate():
    if(sys.platform == 'win32'):
        subprocess.run(f"cmd.exe /K menv\\Scripts\\deactivate.bat", shell=True)
def default():
    print(f'''
    Usage:
        menv init [args] -> create a virtualenv (args are passed to virtualenv)
        menv activate -> activate the virtualenv
        menv deactivate -> deactivate the virtualenv
        menv save -> save the current requirements
        menv start -> install the saved requirements --force to ignore python version
          ''')
params = {
    'init': init,
    'activate':activate,
    'deactivate':deactivate,
    'save': save,
    'start': start,
    'run': run
}

def main():
    if sys.platform.lower() != 'win32':
        print('For now only windows is supported')
    if len(sys.argv) > 1:
        params.get(sys.argv[1], default)()
    else:
        default()
        