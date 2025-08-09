import pypacks

# Example usage of PyPacks

example = pypacks.PyPack()
hello = example.function("hello")
hello.say("Hello")

example.build(pypacks.PyPackType.JAVA)
example.build(pypacks.PyPackType.BEDROCK)
