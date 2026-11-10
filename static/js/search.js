// Render search text through DOM APIs: queries and indexed content are never HTML.
let searchRequest = 0;
async function searchOnChange(event) {
  const query = event.target.value.trim();
  document.querySelectorAll('[data-site-search]').forEach(input => { input.value = event.target.value; });
  const request = ++searchRequest;
  const panel = document.getElementById('search-content');
  const results = document.getElementById('search-results');
  results.replaceChildren(); panel.hidden = !query;
  if (!query) return;
  try {
    if (!window.searchJson) {
      const response = await fetch('/index.json');
      if (!response.ok) throw new Error('Search unavailable');
      window.searchJson = await response.json();
    }
    if (request !== searchRequest) return;
    const matches = window.searchJson.filter(item => [item.title,item.description,item.content].some(text => String(text || '').toLowerCase().includes(query.toLowerCase())));
    if (!matches.length) { results.textContent = `No results found for “${query}”.`; return; }
    matches.forEach(item => {
      const link = document.createElement('a'); link.href = item.permalink;
      const title = document.createElement('strong'); title.textContent = item.title;
      const description = document.createElement('p'); description.textContent = item.description || '';
      link.append(title,description); results.append(link);
    });
  } catch (error) { if (request === searchRequest) results.textContent = 'Search is unavailable. Please use the navigation links.'; }
}
function closeSearch(){searchRequest++;document.getElementById('search-content').hidden=true;document.querySelectorAll('[data-site-search]').forEach(input => {input.value='';});}
document.addEventListener('keydown',event=>{
  if(event.key==='Escape') closeSearch();
  if((event.ctrlKey || event.metaKey) && event.key.toLowerCase()==='k'){
    event.preventDefault();
    if(innerWidth < 992) document.getElementById('navbarContent').classList.add('show');
    const input = [...document.querySelectorAll('[data-site-search]')].find(input=>input.getClientRects().length); input?.focus();
  }
});
document.addEventListener('click',event=>{if(!event.target.closest('[data-site-search],#search-content')) closeSearch();});
