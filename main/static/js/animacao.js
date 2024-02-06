document.addEventListener('DOMContentLoaded', function() {
    // Função para alterar a opacidade quando o elemento estiver visível
    function handleIntersection(entries, observer) {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('animacao-ativa'); // Adiciona uma classe que modifica a opacidade quando o elemento está visível
          observer.unobserve(entry.target);
        }
      });
    }
  
    // Cria um observer para observar as mudanças de interseção
    const observer = new IntersectionObserver(handleIntersection, {
      root: null, // Use a viewport como a área de observação
      rootMargin: '0px', // Não use margem extra
      threshold: 0.5 // Acione quando 50% do elemento estiver visível
    });
  
    // Selecione todos os elementos a serem observados
    const targets = document.querySelectorAll('.animacao');
  
    // Comece a observar todos os elementos
    targets.forEach(target => {
      observer.observe(target);
    });
  });
  