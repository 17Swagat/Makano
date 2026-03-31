import os


# Tool #1
# Tool to connect with the [Sandbox Playground].
# * Be able to create files/folders in the Sandbox.
# * Read/write Files in the Sandbox
class SandboxPlaygroundEnvironment:
    def __init__(self, sandboxFolderPath):
        self.sandboxPath = sandboxFolderPath

    def create_file(self, fname: str):
        with open(os.path.join(self.sandboxPath, fname)) as file:
            file.write("")

    def create_folder(self, fname: str):
        os.makedirs(fname, exist_ok=True)


# Tool #2
# Being Able to do internet search regarding discussed topic for answers.
