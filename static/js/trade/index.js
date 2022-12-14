let nav_flag = 0
document.querySelector('#all-nav-button').addEventListener("click",  function() {
  if(!nav_flag){
    const nav_close = document.querySelector('.all-nav-close')
    nav_close.className = 'all-nav-open'
    const nav_table = document.querySelector('#nav-table')
    nav_table.style.display = 'block'
    nav_flag = 1
  }
  else {
    const nav_close = document.querySelector('.all-nav-open')
    nav_close.className = 'all-nav-close'
    const nav_table = document.querySelector('#nav-table')
    nav_table.style.display = 'none'
    nav_flag = 0
  }
})

const ad_card = document.querySelectorAll('.ad-card')

ad_card.forEach((card, index) => {
  card.addEventListener('mouseover', function() {
    this.querySelector('.ad-card-context').className = 'ad-card-context-hover'
  })
  card.addEventListener('mouseout', function() {
    this.querySelector('.ad-card-context-hover').className = 'ad-card-context'
  })
})

document.querySelector('.trade-index-radio-form').addEventListener("click", function(){
    console.log(document.querySelector('.trade-index-radio-form'))
    var check_id = document.querySelector('input[name="trade"]:checked').id;
    var radios = document.getElementsByName('trade');
    
    for (var i=0; i<radios.length; i++)
    {
      // 체크된 라디오가 현재 인덱스의 id와 같다면
      // -> show
      if (check_id === String(i)) {
        document.querySelector('#trade-card-'+String(i)).setAttribute('style', '')
      }
      // 다르다면
      // -> hide
      else {
        document.querySelector('#trade-card-'+String(i)).setAttribute('style', 'display: none')
      }
    }
})