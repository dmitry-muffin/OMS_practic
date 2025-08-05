function renderAddressTable(data) {
    const tbody = document.querySelector('#address-table tbody');
    tbody.innerHTML = ''; // очистить перед повторной отрисовкой

    data.forEach(item => {
        const tr = document.createElement('tr');

        const tdIndex = document.createElement('td');
        tdIndex.textContent = item.index;

        const tdGroup = document.createElement('td');
        tdGroup.textContent = item.group;

        const tdAddr = document.createElement('td');
        tdAddr.textContent = item.address;

        const tdFound = document.createElement('td');
        tdFound.textContent = item.found ? 'Да' : 'Нет';
        tdFound.style.color = item.found ? 'green' : 'red';

        tr.appendChild(tdIndex);
        tr.appendChild(tdGroup);
        tr.appendChild(tdAddr);
        tr.appendChild(tdFound);

        tbody.appendChild(tr);
    });
}
