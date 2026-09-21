#include <stdio.h>

int main(int argc, char **argv) {
    const char *path = argc > 1 ? argv[1] : "data/generated/topics.tsv";
    FILE *file = fopen(path, "r");
    if (file == NULL) {
        perror(path);
        return 1;
    }

    unsigned long lines = 0;
    int ch;
    while ((ch = fgetc(file)) != EOF) {
        if (ch == '\n') {
            lines++;
        }
    }
    fclose(file);

    if (lines > 0) {
        lines--; /* TSV header */
    }
    printf("topics: %lu\n", lines);
    return 0;
}
