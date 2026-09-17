(()=>{
  const $=(s,r=document)=>r.querySelector(s); const $$=(s,r=document)=>[...r.querySelectorAll(s)];
  const menu=$('[data-menu]'), links=$('[data-links]');
  if(menu&&links){menu.addEventListener('click',()=>{const open=links.classList.toggle('open');menu.setAttribute('aria-expanded',String(open));});}
  $$('.reveal').forEach(el=>{if(!('IntersectionObserver'in window)){el.classList.add('on');return;}const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target);}}),{threshold:.12});io.observe(el);});
  const form=$('[data-demo-form]'); if(form){form.addEventListener('submit',e=>{e.preventDefault();const s=$('[data-form-status]',form);s.textContent='Demo: solicitud simulada. No se transmitió ni guardó ningún dato.';form.reset();});}
  const calc=$('[data-calc]');
  if(calc){const n=id=>Math.max(0,Number($(`[name="${id}"]`,calc).value)||0);const out=(id,v)=>{const el=$(`[data-out="${id}"]`,calc);if(el)el.textContent=v;}; const fmt=n=>new Intl.NumberFormat('es-MX',{style:'currency',currency:'MXN',maximumFractionDigits:0}).format(n); const run=()=>{const leads=n('leads'),book=n('book')/100,show=n('show')/100,close=n('close')/100,ticket=n('ticket'),spend=n('spend');const consults=leads*book*show,procedures=consults*close,revenue=procedures*ticket,roas=spend?revenue/spend:0;out('consults',consults.toFixed(1));out('procedures',procedures.toFixed(1));out('revenue',fmt(revenue));out('roas',roas.toFixed(1)+'×');};$$('input',calc).forEach(i=>i.addEventListener('input',run));run();}
})();
