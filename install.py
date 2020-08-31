import urllib3  # for downloading files
import shutil  # for saving the downloaded files
import re  # for regex, i use it for checking if its a valid url
import os  # i use it for checking os

http = urllib3.PoolManager()
INSTALL_URL = "https://raw.githubusercontent.com/rblxploit/WabzGroupFinder/master/"
urlregex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    # domain...
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)


def isdepsinstalled():
    return shutil.which("node") is not None and shutil.which("npm") is not None


def downloadFile(filename):
    with open(filename, 'wb') as out:
        r = http.request('GET', INSTALL_URL + filename, preload_content=False)
        shutil.copyfileobj(r, out)


def listToEnv(l):
    return "\n".join([f"{el[0]}={el[1]}" for el in l])


def urlinput(t):
    while True:
        c = input(t)
        if len(c) == 0 or re.match(urlregex, c) is None or not c.startswith("https://discord.com/api/webhooks"):
            pass
        else:
            return c


def definput(t, default, av):
    while True:
        c = input(t)
        if len(c) == 0:
            return default
        elif c in av:
            return c


def main():
    runfile = ""
    if os.name == "nt":
        runfile = "runfinder.bat"
    elif os.name == "posix":
        runfile = "./runfinder.sh"
    else:
        print("Your OS might not be compatible with this tool.")
        print("The installation will continue, but it might break.")
    files = ["package.json", "index.js"]
    env = []
    print("Installing Wabz Group Finder...")
    for f in files:
        try:
            downloadFile(f)
        except:
            print(
                f"An error occured for file {f}\nIt might be blocked by the firewall.")
    print("Finished installing base files.")
    env.append(["WEBHOOK_URL", urlinput("Enter discord webhook url: ")])
    env.append(["MODE", definput(
        "Press enter for default (normal) | Enter mode (proxy, normal): ", "normal", ["proxy", "normal"])])
    print("Setting up .env file...")
    envfile = listToEnv(env)
    with open(".env", "w") as fl:
        fl.write(envfile)
    print("Installing dependencies...")
    os.system("npm install")
    if len(runfile) > 0:
        with open(runfile, 'w') as run:
            run.write("node index.js")
        if runfile == "./runfinder.sh":
            os.system("chmod +x runfinder.sh")
        print("The installation is now finished.")
        print(f"To run the file, type: {runfile}")
    else:
        print("The installation is now finished.")
        print("To run the file, type: node index.js")
    print("You could also run it with PM2, but you need to install it.")


if __name__ == "__main__":
    if not isdepsinstalled():
        print("You need to have NodeJS and NPM installed to be able to use this tool.")
        print("Quitting...")
        quit()
    main()
else:
    print("Sorry, but you can't import this file.")
