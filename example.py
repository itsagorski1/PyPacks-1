import pypacks

# Create the PyPack
example = pypacks.PyPack("example", "Example Pack")

# Define a function in the PyPack that says "Hello World!"
hello = pypacks.Function("hello")
hello.add_command("say", "Hello")
hello.add_command("say", "World!")
hello.attach(example)

# Define another function in the PyPack
yello = pypacks.Function("yello")
yello.attach(example)

# Build the PyPack for Bedrock and Java
example.build(pypacks.PyPackType.JAVA, "Example")
example.build(pypacks.PyPackType.BEDROCK, "Example")
