## HackerRank
* Review of `$stdin` and Ruby I/O workings via http://zetcode.com/lang/rubytutorial/io.

## Big O & LRU Cache Review
* Ruby Benchmark gem to test amount of time taken to run something
```
Benchmark.bm do |b|
    b.report("1,000: ") { quick_sort(array) }
end
```

## Vanilla JS 30
### Drum kit project
* Became familiar with an audio element and learned out to play a sound
* Added vanilla JS event listener to the window and to other elements: `window.addEventListener('keydown', playSound);`.
* Learned about event property types, specifically: `event.propertyName !== transform`.

## SF JavaScript Meetup
### GRAND Stack @ MuleSoft
GraphQL, React, Apollo, Neo4j
* GraphQL is basically a querying language for APIs.
* Neo4j is a graph database (rather than a tabular one). Syncs nicely with GraphQL because GraphQL uses a database as a graph.
* If using GraphQL with a non-graph database, you need to use a resolver to allow GraphQL to traverse the table like a graph.
* A big advantage of GraphQL is that it doesn't use joins, which can become very complex after several joins. Instead, it uses relationships between nodes, so it can traverse through the graph and find specific data you're looking for rather than return a massive multi-joined table when you are only trying to return one value.