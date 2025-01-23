(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner(0);

    // Event carousel
    $(document).ready(function () {
        var $carousel = $(".event-carousel");
        var itemCount = $carousel.find(".event-item").length;

        if (itemCount < 3) {
            // Fewer than 3 events: Disable carousel and center cards
            $carousel.addClass("fewer-than-3");
        } else {
            // 3 or more events: Enable carousel
            $carousel.owlCarousel({
                autoplay: true,
                smartSpeed: 1000,
                center: false,
                dots: false,
                loop: false, // Disable looping
                margin: 25,
                nav: true, // Enable navigation arrows
                navText: [
                    '<i class="fas fa-arrow-left"></i>',
                    '<i class="fas fa-arrow-right"></i>'
                ],
                responsiveClass: true,
                responsive: {
                    0: {
                        items: 1,
                        nav: true
                    },
                    768: {
                        items: 2,
                        nav: true
                    },
                    1200: {
                        items: 3,
                        nav: true
                    }
                }
            });
        }

        // Initialize DataTable for tenders table
        $('#tenders-table').DataTable({
            columnDefs: [
                { orderable: true, targets: [0, 1, 2, 3] }, // Allow sorting for Title, Description, Deadline, Status
                { orderable: false, targets: [4] } // Disable sorting for Download column
            ],
            order: [[2, 'asc']], // Default sort by Deadline (ascending)
            responsive: true // Enable DataTable's built-in responsiveness
        });

        // Add data-label attributes for mobile responsiveness
        const table = document.getElementById('tenders-table');
        if (table) {
            const headers = table.querySelectorAll('th');
            table.querySelectorAll('tbody tr').forEach(row => {
                row.querySelectorAll('td').forEach((cell, index) => {
                    cell.setAttribute('data-label', headers[index].textContent);
                });
            });
        }
    });

    // Back to top button
    $(window).scroll(function () {
    if ($(this).scrollTop() > 300) {
        $('.back-to-top').fadeIn('slow');
    } else {
        $('.back-to-top').fadeOut('slow');
    }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });

    // Sponsors Scroll Functionality
    const sponsorsScrollContainer = document.querySelector('.sponsors-scroll-container');
    if (sponsorsScrollContainer) {
        let scrollInterval;
        const scrollSpeed = 40; // Adjust scroll speed
        const scrollThreshold = 100; // Distance from the edge to trigger scrolling

        function scrollLeft() {
            sponsorsScrollContainer.scrollBy({ left: -scrollSpeed, behavior: 'smooth' });
        }

        function scrollRight() {
            sponsorsScrollContainer.scrollBy({ left: scrollSpeed, behavior: 'smooth' });
        }

        sponsorsScrollContainer.addEventListener('mousemove', (e) => {
            const rect = sponsorsScrollContainer.getBoundingClientRect();
            const mouseX = e.clientX - rect.left;

            console.log('Mouse X:', mouseX); // Debugging

            clearInterval(scrollInterval);

            if (mouseX < scrollThreshold) {
                console.log('Scrolling left'); // Debugging
                scrollInterval = setInterval(scrollLeft, 50);
            } else if (mouseX > rect.width - scrollThreshold) {
                console.log('Scrolling right'); // Debugging
                scrollInterval = setInterval(scrollRight, 50);
            }
        });

        sponsorsScrollContainer.addEventListener('mouseleave', () => {
            clearInterval(scrollInterval);
        });

        let isDragging = false;
        let startX, initialScrollLeft;

        sponsorsScrollContainer.addEventListener('touchstart', (e) => {
            isDragging = true;
            startX = e.touches[0].pageX - sponsorsScrollContainer.offsetLeft;
            initialScrollLeft = sponsorsScrollContainer.scrollLeft;
        });

        sponsorsScrollContainer.addEventListener('touchmove', (e) => {
            if (!isDragging) return;
            e.preventDefault();
            const x = e.touches[0].pageX - sponsorsScrollContainer.offsetLeft;
            const walk = (x - startX) * 2;
            sponsorsScrollContainer.scrollLeft = initialScrollLeft - walk;
        });

        sponsorsScrollContainer.addEventListener('touchend', () => {
            isDragging = false;
        });
    }

    // Toggle Points Functionality
    function togglePoints(button, id) {
    const pointsContainer = button.previousElementSibling;
    const allPoints = pointsContainer.querySelectorAll('.services-page__points-item');
    const hiddenPoints = pointsContainer.querySelectorAll('.services-page__points-item.hidden');

    if (button.textContent === "MORE") {
        // Show all points
        hiddenPoints.forEach(point => point.classList.remove('hidden'));
        button.textContent = "LESS";
    } else {
        // Hide all points except the first 4
        allPoints.forEach((point, index) => {
            if (index >= 4) {
                point.classList.add('hidden');
            }
        });
        button.textContent = "MORE";
    }
}

    // Attach togglePoints to the global window object if needed
    window.togglePoints = togglePoints;

})(jQuery);