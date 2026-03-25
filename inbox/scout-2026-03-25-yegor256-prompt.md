---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code CLAUDE.md"
  quality_score: 65
  scoring_breakdown:
    stars: 18
    recency: 25
    docs: 15
    community: 7
github_data:
  full_name: "yegor256/prompt"
  url: "https://github.com/yegor256/prompt"
  description: "A plain-text prompt for LLMs that teaches the essence of elegant coding and testing—save it to ~/.claude/CLAUDE.md."
  stars: 136
  forks: 12
  open_issues: 5
  language: ""
  license: "MIT"
  last_push: "2026-03-25"
  created: "2025-06-24"
  topics: ["ai", "llm", "prompt-engineering", "vibe-coding"]
---

# yegor256/prompt

> Discovered by arsenal scout — awaiting manual triage

## Description

A plain-text prompt for LLMs that teaches the essence of elegant coding and testing—save it to ~/.claude/CLAUDE.md.

## README Excerpt

My pronoun is HE/HIM, not THEY/THEM.
My name is Yegor, call me by name.

Always use GNU tools, like gsed, gfind, ggrep, gcat, etc.
Don't change existing code structure without a strong reason.
Reproduce a bug or a feature with a unit or integration test and only then fix it.

If a problem is hard to fix, don't hesitate to use extensive debug-logging.

Don't use inline code comments or ANY kind of comments in source code files, avoid codeblocks on top of classes and methods.
Prepent every class with a docblock that explains the purpose of the class and provides usage examples.
Use English only to write doclbocks, using only ASCII.

Respect the DDD paradigm.
Respect Elegant Objects design principles.
Respect the principles of testing in the "Angry Tests" book of Yegor Bugayenko.
Respect the principle of "Paired Brackets" suggested by Yegor Bugayenko.
Favor "fail fast" paradigm over "fail safe": throw exception earlier.

Don't put any code in constructors except assignment statements.
Use only one primary constructor per class; delegate from secondary constructors to it.
Encapsulate no more than four attributes per class.
Encapsulate at least one attribute per class.
Declare all classes as final, prohibiting inheritance.
Avoid implementation inheritance at all costs (not to be confused with subtyping).
Don't use the -er suffix in class names: don't create Managers, Controllers, Routers, Readers, and Writers.
Don't create utility classes.
Don't use static methods in classes.
Don't use public static literals in classes.

Avoid setters, as they make objects mutable.
Avoid getters, as they are symptoms of an anemic object model.
Favor immutable objects over mutable ones.
Never change attributes after assignment.

Use single nouns for variable names, never use compound or composite names.
Use single verbs for method names, never compound or composite.
Name methods according to CQRS principle: use either nouns or verbs.
Declare methods in interfaces and then implement them in classes.
Avoid public methods that do not implement an interface.
Don't put black lines into method bodies.
Never return null from methods.
Avoid checking incoming arguments for validity in methods.
Never pass null as an argument.
Don't use type introspection or type casting.
Don't use reflection on object internals.

Don't end error and log messages with a period.
Keep error and log messages as single sentences, with no periods inside.
Include as much context as possible in exception messages.

Cover every change with a unit test to guarantee repeatability.
Put only one assertion in every test case.
Place the assertion as the last statement in every test.
Assert at least once in every test.
Keep test cases as short as possible.
Aim for tests that consist of a single statement.
Verify only one specific behavioral pattern per test.
Include a failure message in every assertion that is a negatively toned claim about the error.

Map each test file one-to-one with the feature file it test

## Links

- Repository: https://github.com/yegor256/prompt
