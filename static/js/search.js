function handleSortChange() {
    const selectElement = document.getElementById('sort-by-select');
    const selectedValue = selectElement.value;
    const currentUrl = window.location.href;
    const baseUrl = currentUrl.split('?')[0];
    const queryParams = new URLSearchParams(window.location.search);
    queryParams.set('sort_by', selectedValue);
    const newUrl = `${baseUrl}?${queryParams.toString()}`;
    window.location.href = newUrl;
}