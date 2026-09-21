package main

import (
    "bufio"
    "fmt"
    "os"
    "strings"
)

func main() {
    path := "data/generated/topics.tsv"
    if len(os.Args) > 1 {
        path = os.Args[1]
    }

    file, err := os.Open(path)
    if err != nil {
        panic(err)
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)
    rows := 0
    difficulty := map[string]int{}
    first := true
    for scanner.Scan() {
        if first {
            first = false
            continue
        }
        fields := strings.Split(scanner.Text(), "\t")
        if len(fields) < 5 {
            continue
        }
        rows++
        difficulty[fields[4]]++
    }
    if err := scanner.Err(); err != nil {
        panic(err)
    }

    fmt.Printf("topics: %d\n", rows)
    fmt.Printf("difficulty: %v\n", difficulty)
}
