### A Pluto.jl notebook ###
# Foundation notebook source; it can also be executed as a Julia script.

using Pkg
Pkg.activate(joinpath(@__DIR__, ".."))

include(joinpath(@__DIR__, "..", "src", "PolyglotKnowledge.jl"))
using .PolyglotKnowledge

root = normpath(joinpath(@__DIR__, "..", ".."))
relations = load_relations(joinpath(root, "data", "generated", "relations.tsv"))
graph = adjacency(relations)
centrality = degree_centrality(graph)

top = sort(collect(centrality), by = last, rev = true)[1:min(10, length(centrality))]
println("Top seed nodes by degree centrality:")
foreach(println, top)
