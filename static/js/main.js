// --- Lightbox init ---
(function(){
  console.log('main.js loaded');

  const box = document.querySelector('.lightbox');
  const imgEl = box ? box.querySelector('.lightbox-img') : null;
  const closeBtn = box ? box.querySelector('.lightbox-close') : null;

  if(!box || !imgEl){
    console.warn('Lightbox контейнер не найден. Проверьте base.html.');
    return;
  }

  // Открытие по клику на любую картинку в masonry
  document.addEventListener('click', (e)=>{
    const img = e.target.closest('.masonry-item img, .masonry img');
    if(!img) return;

    // если картинка обёрнута в <a>, глушим переход
    const link = e.target.closest('a');
    if(link) e.preventDefault();

    imgEl.src = img.currentSrc || img.src;
    box.classList.add('open');
    box.setAttribute('aria-hidden','false');
  });

   Закрытие: по кнопке/фону
  document.addEventListener('click', (e)=>{
    if(e.target.closest('.lightbox-close') || e.target === box){
      box.classList.remove('open');
      box.setAttribute('aria-hidden','true');
      imgEl.removeAttribute('src');
    }
  });

  // Закрытие по Esc
  document.addEventListener('keydown', (e)=>{
    if(e.key === 'Escape' && box.classList.contains('open')){
      box.classList.remove('open');
      box.setAttribute('aria-hidden','true');
      imgEl.removeAttribute('src');
    }
  });
})();