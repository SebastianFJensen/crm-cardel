document.addEventListener('DOMContentLoaded', () => {
    const activityButtons = document.querySelectorAll('.activity-button');
    const activityContents = document.querySelectorAll('.activity-content');
    let activeButton = null;
  
    // Select the first button by default
    activeButton = activityButtons[0];
    activeButton.classList.add('active');
  
    // Show all activity items by default
    activityContents.forEach((content) => {
      if (content.dataset.activity === 'all') {
        content.style.display = 'block';
      } else {
        content.style.display = 'none';
      }
    });
  
    activityButtons.forEach((button) => {
      button.addEventListener('click', (e) => {
        // Remove the 'active' class from the previously active button
        if (activeButton) {
          activeButton.classList.remove('active');
        }
  
        // Add the 'active' class to the selected button
        activeButton = e.target;
        activeButton.classList.add('active');
  
        const activity = e.target.getAttribute('data-activity');
  
        activityContents.forEach((content) => {
          if (activity === 'all') {
            if (content.dataset.activity === 'all') {
              content.style.display = 'block';
              const allActivityContentContainer = document.querySelector('.activity-content[data-activity="all"]');
              const activityItems = allActivityContentContainer.querySelectorAll('.activity-item');
  
              if (activityItems.length > 5) {
                const sets = allActivityContentContainer.querySelectorAll('.element-set');
                sets.forEach((set) => set.style.display = 'none');
                sets[0].style.display = 'block';
  
                const circles = document.querySelectorAll(".circle");
                circles.forEach((circle) => circle.classList.remove('active'));
                circles[0].classList.add('active');
              }
            } else {
              content.style.display = 'none';
            }
          } else if (content.dataset.activity === activity) {
            content.style.display = 'block';
          } else {
            content.style.display = 'none';
          }
        });
      });
    });
  
    const allActivityContentContainer = document.querySelector('.activity-content[data-activity="all"]');
    const activityItems = allActivityContentContainer.querySelectorAll('.activity-item');
  
    if (activityItems.length > 5) {
      const numSets = Math.ceil(activityItems.length / 5);
  
      for (let i = 0; i < numSets; i++) {
        const setId = `set-${i + 1}`;
        const set = document.createElement("div");
        set.id = setId;
        set.className = "element-set";
  
        let numElements = 0;
        for (let j = 0; j < 5; j++) {
          const elementIndex = i * 5 + j;
          if (elementIndex < activityItems.length) {
            const element = activityItems[elementIndex];
            set.appendChild(element);
            numElements++;
          } else {
            for (let k = 0; k < 5 - numElements; k++) {
              const element = document.createElement("br");
              set.appendChild(element);
            }
            break;
          }
        }
  
        allActivityContentContainer.appendChild(set);
  
        if (i > 0) {
          set.style.display = "none";
        }
      }
  
      const circles = document.querySelectorAll(".circle");
      circles.forEach((circle, index) => {
        circle.addEventListener("click", () => {
          const setId = `set-${index + 1}`;
          const set = document.getElementById(setId);
  
          allActivityContentContainer.querySelectorAll(".element-set").forEach((elementSet) => {
            elementSet.style.display = "none";
          });
  
          set.style.display = "block";
  
          circles.forEach((circle) => {
            circle.classList.remove("active");
          });
  
          circle.classList.add("active");
        });
      });
  
      let startX, scrollLeft;
  
      allActivityContentContainer.addEventListener('touchstart', (e) => {
        startX = e.touches[0].clientX;
        scrollLeft = allActivityContentContainer.scrollLeft;
      });
  
      allActivityContentContainer.addEventListener('touchend', (e) => {
        const endX = e.changedTouches[0].clientX;
        const distance = (startX - endX);
  
        if (Math.abs(distance) > 50) {
          const sets = allActivityContentContainer.querySelectorAll('.element-set');
          let currentSetIndex = Array.from(sets).findIndex((set) => set.style.display === 'block');
  
          if (distance > 0) {
            currentSetIndex++;
            if (currentSetIndex >= sets.length) currentSetIndex = 0;
          } else {
            currentSetIndex--;
            if (currentSetIndex < 0) currentSetIndex = sets.length - 1;
          }
  
          sets.forEach((set) => set.style.display = 'none');
          sets[currentSetIndex].style.display = 'block';
  
          circles.forEach((circle) => circle.classList.remove('active'));
          circles[currentSetIndex].classList.add('active');
        }
      });
    }
  
    // Trigger a click event on the first circle when entering the page
    document.querySelectorAll('.circle')[0].click();
  
    const ellipsis = document.querySelector('.ellipsis');
    const dropdown = document.querySelector('.dropdown');
  
    ellipsis.addEventListener('click', (event) => {
      event.stopPropagation(); // prevent event from bubbling up to document
      dropdown.classList.toggle('active');
    });
  
    const dropdownItems = document.querySelectorAll('.dropdown-item');
  
    dropdownItems.forEach((item) => {
      item.addEventListener('click', () => {
        console.log(`Clicked on ${item.textContent}`);
        dropdown.classList.remove('active');
      });
    });
  
    // Add event listener to document to close dropdown when clicking outside
    document.addEventListener('click', (event) => {
      if (!ellipsis.contains(event.target) &&!dropdown.contains(event.target)) {
        dropdown.classList.remove('active');
      }
    });
  });