const ORDER_BORDER_COLORS = {
  "🐂": "#6b8e23",
  "⛽": "#c0392b",
  "🦋": "#8e44ad",
  "🏟": "#d35400",
  "🌾": "#2e8b57",
  "⚖": "#4682b4",
  "🖼": "#7f8c8d"
};

function pct(done, total) {
  return total > 0 ? (done / total) * 100 : 0;
}

function renderProgress(data) {
  const p = pct(data.card_generated, data.card_total);
  document.getElementById("card-progress-text").textContent =
    `${"█".repeat(Math.round(p / 4))}${"░".repeat(25 - Math.round(p / 4))} ${data.card_generated} / ${data.card_total} (${p.toFixed(1)}%)`;
  document.getElementById("card-progress-fill").style.width = `${p}%`;
}

function renderGrid(data) {
  const axisHeading = document.getElementById("axis-headings");
  const deckGrid = document.getElementById("deck-grid");

  const firstRow = data.deck_grid.slice(0, 6);
  firstRow.forEach((entry) => {
    const el = document.createElement("div");
    el.textContent = `${entry.axis} ${entry.axis_name}`;
    axisHeading.appendChild(el);
  });

  data.deck_grid.forEach((entry) => {
    const cell = document.createElement("div");
    const ratio = entry.generated / entry.total;
    const state = ratio === 0 ? "empty" : ratio >= 1 ? "complete" : "partial";
    cell.className = `deck-cell ${state}`;
    cell.style.borderColor = ORDER_BORDER_COLORS[entry.order] || "#555";
    cell.textContent = `${String(entry.deck).padStart(2, "0")}: ${entry.generated}/${entry.total}\n${entry.order} ${entry.order_name}`;
    deckGrid.appendChild(cell);
  });
}

function renderColorSections(data) {
  const host = document.getElementById("color-summary");
  data.color_sections.forEach((section) => {
    const total = section.done + section.open;
    const row = document.createElement("div");
    row.className = "color-row";
    row.innerHTML = `
      <div class="color-top">
        <span>${section.emoji} ${section.name}</span>
        <span>${section.done} done / ${section.open} open</span>
      </div>
      <div class="color-bar"><div class="color-bar-fill" style="width:${pct(section.done, total)}%"></div></div>
    `;
    host.appendChild(row);
  });
}

function renderCx(data) {
  document.getElementById("cx-counter").textContent = `${data.cx_done} / ${data.cx_total} containers complete`;
}

function renderFooter(data) {
  document.getElementById("last-updated").textContent =
    `Last updated: ${data.last_updated}. Data generated from repo state.`;
}

async function init() {
  const response = await fetch("data/progress.json");
  const data = await response.json();
  renderProgress(data);
  renderGrid(data);
  renderColorSections(data);
  renderCx(data);
  renderFooter(data);
}

init();
