const loadButton = document.getElementById('load');
const filesEl = document.getElementById('files');

function renderFiles(files) {
    filesEl.innerHTML = '';
    for (const file of files) {
        const item = document.createElement('li');
        item.innerHTML = `<strong>${file.name}</strong><span>${file.suffix} · ${file.size} bytes</span>`;
        filesEl.appendChild(item);
    }
}

async function loadFiles() {
    const files = await window.pywebview.api.list_files();
    renderFiles(files);
}

window.addEventListener('pywebviewready', loadFiles);
loadButton.addEventListener('click', loadFiles);