// Funcionalidad del JavaScript para la aplicación

document.addEventListener('DOMContentLoaded', function() {
    // Inicializar tooltips de Bootstrap
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    });

    // Validación del formulario de orientación vocacional
    const formOrientacion = document.getElementById('formOrientacion');
    if (formOrientacion) {
        formOrientacion.addEventListener('submit', function(event) {
            let isValid = true;
            const textareas = formOrientacion.querySelectorAll('textarea[required]');
            const inputs = formOrientacion.querySelectorAll('input[required]');

            // Validar textareas
            textareas.forEach(function(textarea) {
                if (textarea.value.trim().length < 10) {
                    isValid = false;
                    textarea.classList.add('is-invalid');

                    // Crear mensaje de error si no existe
                    if (!textarea.nextElementSibling || !textarea.nextElementSibling.classList.contains('invalid-feedback')) {
                        const feedback = document.createElement('div');
                        feedback.classList.add('invalid-feedback');
                        feedback.textContent = 'Por favor, proporciona una respuesta más detallada (mínimo 10 caracteres).';
                        textarea.parentNode.insertBefore(feedback, textarea.nextSibling);
                    }
                } else {
                    textarea.classList.remove('is-invalid');
                }
            });

            // Validar inputs
            inputs.forEach(function(input) {
                if (input.value.trim() === '') {
                    isValid = false;
                    input.classList.add('is-invalid');

                    // Crear mensaje de error si no existe
                    if (!input.nextElementSibling || !input.nextElementSibling.classList.contains('invalid-feedback')) {
                        const feedback = document.createElement('div');
                        feedback.classList.add('invalid-feedback');
                        feedback.textContent = 'Este campo es obligatorio.';
                        input.parentNode.insertBefore(feedback, input.nextSibling);
                    }
                } else {
                    input.classList.remove('is-invalid');
                }
            });

            // Mostrar mensaje de carga si el formulario es válido
            if (isValid) {
                // Deshabilitar el botón de envío
                const submitBtn = formOrientacion.querySelector('button[type="submit"]');
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>Procesando...';

                // Mostrar mensaje de carga
                const loadingAlert = document.createElement('div');
                loadingAlert.classList.add('alert', 'alert-info', 'mt-3');
                loadingAlert.innerHTML = '<i class="fas fa-info-circle me-2"></i>Estamos analizando tus respuestas. Este proceso puede tardar unos segundos...';
                formOrientacion.appendChild(loadingAlert);
            } else {
                event.preventDefault();
            }
        });

        // Eliminar clases de error en focus
        const allInputs = formOrientacion.querySelectorAll('input, textarea');
        allInputs.forEach(function(input) {
            input.addEventListener('focus', function() {
                this.classList.remove('is-invalid');
            });
        });
    }

    // Funcionalidad para la página de resultados - gráfico de compatibilidad
    const resultadosContainer = document.getElementById('listaRecomendaciones');
    if (resultadosContainer) {
        // Si hay gráficos o visualizaciones, aquí se inicializarían
        console.log('Página de resultados cargada');
    }
});

