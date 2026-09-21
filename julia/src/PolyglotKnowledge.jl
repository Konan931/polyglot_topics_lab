module PolyglotKnowledge

using DelimitedFiles
using Statistics

export TopicTable, RelationTable, load_topics, load_relations, adjacency, degree_centrality, shortest_path

struct TopicTable
    header::Vector{String}
    rows::Vector{Vector{String}}
end

struct RelationTable
    header::Vector{String}
    rows::Vector{Vector{String}}
end

function read_tsv(path::AbstractString)
    raw = readdlm(path, '\t', String, '\n')
    header = vec(raw[1, :])
    rows = [vec(raw[i, :]) for i in 2:size(raw, 1)]
    return header, rows
end

function load_topics(path::AbstractString)
    header, rows = read_tsv(path)
    TopicTable(header, rows)
end

function load_relations(path::AbstractString)
    header, rows = read_tsv(path)
    RelationTable(header, rows)
end

function column_index(header::Vector{String}, name::String)
    index = findfirst(==(name), header)
    isnothing(index) && error("missing column: $name")
    return index
end

function adjacency(relations::RelationTable)
    source_col = column_index(relations.header, "source_id")
    target_col = column_index(relations.header, "target_id")
    graph = Dict{String, Set{String}}()
    for row in relations.rows
        source = row[source_col]
        target = row[target_col]
        push!(get!(graph, source, Set{String}()), target)
        push!(get!(graph, target, Set{String}()), source)
    end
    graph
end

function degree_centrality(graph::Dict{String, Set{String}})
    n = max(length(graph) - 1, 1)
    Dict(node => length(neighbors) / n for (node, neighbors) in graph)
end

function shortest_path(graph::Dict{String, Set{String}}, source::String, target::String)
    source == target && return [source]
    queue = [source]
    previous = Dict{String, Union{Nothing, String}}(source => nothing)
    cursor = 1
    while cursor <= length(queue)
        node = queue[cursor]
        cursor += 1
        for neighbor in get(graph, node, Set{String}())
            haskey(previous, neighbor) && continue
            previous[neighbor] = node
            neighbor == target && break
            push!(queue, neighbor)
        end
        haskey(previous, target) && break
    end
    haskey(previous, target) || return String[]
    path = String[target]
    while previous[path[end]] !== nothing
        push!(path, previous[path[end]]::String)
    end
    reverse(path)
end

end
