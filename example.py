import pypacks

# Create the PyPack
example = pypacks.PyPack()

# Define a function in the PyPack that says "Hello"
hello = example.function("hello")
hello.say("Hello")

# Build the PyPack for Bedrock and Java
example.build(pypacks.PyPackType.JAVA)
example.build(pypacks.PyPackType.BEDROCK)
