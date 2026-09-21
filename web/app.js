const status = document.querySelector('#status');
const search = document.querySelector('#search');
const grid = document.querySelector('#topics');

function parseTSV(text) {
  const [header, ...rows] = text.trim().split('\n').map(line => line.split('\t'));
  return rows.map(row => Object.fromEntries(header.map((key, index) => [key, row[index] ?? ''])));
}

const response = await fetch('../data/generated/topics.tsv');
const topics = parseTSV(await response.text());

function render() {
  const query = search.value.trim().toLocaleLowerCase('de');
  const filtered = topics.filter(topic => !query || `${topic.canonical_name} ${topic.categories} ${topic.summary_short}`.toLocaleLowerCase('de').includes(query));
  status.textContent = `${filtered.length} / ${topics.length} topics`;
  grid.replaceChildren(...filtered.slice(0, 120).map(topic => {
    const card = document.createElement('article');
    const title = document.createElement('h2');
    title.textContent = topic.canonical_name;
    const summary = document.createElement('p');
    summary.textContent = topic.summary_short;
    const meta = document.createElement('p');
    meta.className = 'meta';
    meta.textContent = `${topic.categories} · difficulty ${topic.difficulty} · ${topic.metadata_status}`;
    card.append(title, summary, meta);
    return card;
  }));
}

search.addEventListener('input', render);
render();
