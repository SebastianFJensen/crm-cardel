const fileExplorer = document.getElementById('file-explorer');
const filesList = document.getElementById('files-list');
let draggedFile = null;

filesList.addEventListener('dragover', (event) => {
  event.preventDefault();
  event.dataTransfer.dropEffect = 'move';
});

filesList.addEventListener('drop', (event) => {
  event.preventDefault();
  const files = event.dataTransfer.files;
  handleFileDrop(files);
});

function handleFileDrop(files) {
  for (let i = 0; i < files.length; i++) {
    const file = files[i];
    const fileItem = createFileItem(file);
    filesList.appendChild(fileItem);
    addFileListeners(fileItem, file);
  }
}

function createFileItem(file) {
  const fileItem = document.createElement('div');
  fileItem.classList.add('file-item');
  fileItem.draggable = true;

  const fileName = document.createElement('p');
  fileName.classList.add('file-name');
  fileName.textContent = file.name;

  fileItem.appendChild(fileName);

  return fileItem;
}

function addFileListeners(fileItem, file) {
  fileItem.addEventListener('dragstart', (event) => {
    event.dataTransfer.setData('text/plain', '');
    draggedFile = file;
  });

  fileItem.addEventListener('dragover', (event) => {
    event.preventDefault();
  });

  fileItem.addEventListener('drop', (event) => {
    event.preventDefault();
    const files = event.dataTransfer.files;
    handleFileDrop(files);
  });

  fileItem.addEventListener('click', () => {
    if (file.type.startsWith('image/')) {
      const preview = document.createElement('img');
      preview.src = URL.createObjectURL(file);
      preview.style.width = '100%';
      preview.style.height = 'auto';
      fileExplorer.appendChild(preview);
    }
  });
}
const renameInput = document.getElementById('rename-input');
const renameButton = document.getElementById('rename-button');

renameButton.addEventListener('click', () => {
  const newName = renameInput.value;
  if (newName && draggedFile) {
    draggedFile.name = newName;
    renameInput.style.display = 'none';
    renameButton.style.display = 'none';
    draggedFile.parentElement.querySelector('.file-name').textContent = newName;
  }
});

filesList.addEventListener('click', (event) => {
  if (event.target.tagName === 'P' && event.target.classList.contains('file-name')) {
    renameInput.value = event.target.textContent;
    renameInput.style.display = 'block';
    renameButton.style.display = 'block';
    draggedFile = event.target.parentElement;
  }
});
const deleteButton = document.getElementById('delete-button');

deleteButton.addEventListener('click', () => {
  if (draggedFile) {
    draggedFile.remove();
    draggedFile = null;
  }
});

filesList.addEventListener('click', (event) => {
  if (event.target.tagName === 'BUTTON' && event.target.id === 'delete-button') {
    event.target.parentElement.parentElement.remove();
    draggedFile = null;
  }
});
