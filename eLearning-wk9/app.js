// Basic in-memory course data; persisted progress per user in localStorage
const courses = [
    {
        id: 'js-basics',
        title: 'JavaScript Basics',
        description: 'Learn variables, functions, and control flow in modern JS.',
        lessons: [
            { id: 'js-1', title: 'Intro to JS' },
            { id: 'js-2', title: 'Variables & Types' },
            { id: 'js-3', title: 'Functions' },
            { id: 'js-4', title: 'Control Flow' }
        ]
    },
    {
        id: 'html-css',
        title: 'HTML & CSS Fundamentals',
        description: 'Structure content with HTML and style it with CSS.',
        lessons: [
            { id: 'hc-1', title: 'Semantic HTML' },
            { id: 'hc-2', title: 'Box Model' },
            { id: 'hc-3', title: 'Flexbox & Grid' }
        ]
    },
    {
        id: 'git-github',
        title: 'Git & GitHub',
        description: 'Version control essentials and collaborating with GitHub.',
        lessons: [
            { id: 'gg-1', title: 'Git Basics' },
            { id: 'gg-2', title: 'Branching & Merging' },
            { id: 'gg-3', title: 'Pull Requests' }
        ]
    }
];

// --- Simple state & persistence helpers ---
const storage = {
    getUser() {
        const raw = localStorage.getItem('miniEL_user');
        return raw ? JSON.parse(raw) : null;
    },
    setUser(user) {
        localStorage.setItem('miniEL_user', JSON.stringify(user));
    },
    clearUser() { localStorage.removeItem('miniEL_user'); },
    getProgress(userId) {
        const raw = localStorage.getItem(`miniEL_progress_${userId}`);
        return raw ? JSON.parse(raw) : { courses: {} };
    },
    setProgress(userId, progress) {
        localStorage.setItem(`miniEL_progress_${userId}`, JSON.stringify(progress));
    }
};

// Router: #/ (home), #/course/:id, #/login
function navigateTo(hash) {
    if (location.hash !== hash) location.hash = hash;
    else render();
}

window.addEventListener('hashchange', render);
window.addEventListener('DOMContentLoaded', () => {
    wireGlobalNav();
    if (!location.hash) navigateTo('#/');
    else render();
});

function wireGlobalNav() {
    const homeNav = document.getElementById('nav-home');
    homeNav.addEventListener('click', () => navigateTo('#/'));
    homeNav.addEventListener('keydown', (e) => { if (e.key === 'Enter') navigateTo('#/'); });

    const loginBtn = document.getElementById('login-btn');
    const logoutBtn = document.getElementById('logout-btn');
    const greet = document.getElementById('user-greeting');

    const syncAuthUI = () => {
        const user = storage.getUser();
        if (user) {
            greet.textContent = `Hi, ${user.email}`;
            loginBtn.style.display = 'none';
            logoutBtn.style.display = 'inline-flex';
        } else {
            greet.textContent = '';
            loginBtn.style.display = 'inline-flex';
            logoutBtn.style.display = 'none';
        }
    };

    loginBtn.addEventListener('click', () => navigateTo('#/login'));
    logoutBtn.addEventListener('click', () => { storage.clearUser(); syncAuthUI(); render(); });

    syncAuthUI();
}

function render() {
    const root = document.getElementById('app-root');
    const route = location.hash.replace('#', '');

    if (route.startsWith('/course/')) {
        const id = route.split('/course/')[1];
        renderCourse(root, id);
        return;
    }
    if (route.startsWith('/login')) {
        renderAuth(root);
        return;
    }
    renderHome(root);
}

// --- Views ---
function renderHome(root) {
    const tpl = document.getElementById('tpl-home');
    root.innerHTML = '';
    root.appendChild(tpl.content.cloneNode(true));

    const list = document.getElementById('course-list');
    const user = storage.getUser();
    const progress = user ? storage.getProgress(user.email) : { courses: {} };

    courses.forEach(course => {
        const card = document.createElement('article');
        card.className = 'course-card';
        card.innerHTML = `
            <h3>${course.title}</h3>
            <p>${course.description}</p>
            <div class="course-meta">
                <span class="muted">${course.lessons.length} lessons</span>
                <span class="badge">${getCourseProgressPercent(progress, course.id)}% done</span>
            </div>
        `;
        const isCompleted = !!progress.courses[course.id]?.completed;
        if (isCompleted) {
            const badge = document.createElement('span');
            badge.className = 'badge success';
            badge.textContent = 'Completed';
            card.querySelector('.course-meta').appendChild(badge);
        }
        card.addEventListener('click', () => navigateTo(`#/course/${course.id}`));
        list.appendChild(card);
    });
}

function renderCourse(root, courseId) {
    const course = courses.find(c => c.id === courseId);
    if (!course) {
        root.innerHTML = '<p>Course not found.</p>';
        return;
    }

    const tpl = document.getElementById('tpl-course');
    root.innerHTML = '';
    root.appendChild(tpl.content.cloneNode(true));

    document.getElementById('course-title').textContent = course.title;
    document.getElementById('course-desc').textContent = course.description;

    const user = storage.getUser();
    const userId = user ? user.email : 'guest';
    const progress = storage.getProgress(userId);
    progress.courses[courseId] = progress.courses[courseId] || { completed: false, completedLessons: [] };

    const lessonList = document.getElementById('lesson-list');
    course.lessons.forEach(lesson => {
        const li = document.createElement('li');
        li.className = 'lesson-item';
        const isChecked = progress.courses[courseId].completedLessons.includes(lesson.id);
        li.innerHTML = `
            <div class="title">
                <input type="checkbox" ${isChecked ? 'checked' : ''} aria-label="Mark lesson complete">
                <span>${lesson.title}</span>
            </div>
            <span class="badge">${isChecked ? 'Done' : 'Todo'}</span>
        `;
        const checkbox = li.querySelector('input');
        checkbox.addEventListener('change', () => {
            toggleLesson(progress, userId, courseId, lesson.id, checkbox.checked);
            updateProgressUI(progress, courseId);
            // if all lessons checked, set completed true
            progress.courses[courseId].completed = course.lessons.every(l => progress.courses[courseId].completedLessons.includes(l.id));
            storage.setProgress(userId, progress);
            render(); // refresh to update badges
        });
        lessonList.appendChild(li);
    });

    // progress UI
    updateProgressUI(progress, courseId);

    document.getElementById('back-btn').addEventListener('click', () => navigateTo('#/'));
    const completeBtn = document.getElementById('complete-course-btn');
    completeBtn.addEventListener('click', () => {
        progress.courses[courseId].completed = true;
        // mark all lessons as completed
        progress.courses[courseId].completedLessons = course.lessons.map(l => l.id);
        storage.setProgress(userId, progress);
        updateProgressUI(progress, courseId);
        render();
    });
}

function updateProgressUI(progress, courseId) {
    const percent = getCourseProgressPercent(progress, courseId);
    const fill = document.getElementById('progress-fill');
    const text = document.getElementById('progress-text');
    if (fill) fill.style.width = `${percent}%`;
    if (text) text.textContent = `${percent}% complete`;
}

function toggleLesson(progress, userId, courseId, lessonId, isChecked) {
    const list = new Set(progress.courses[courseId].completedLessons);
    if (isChecked) list.add(lessonId); else list.delete(lessonId);
    progress.courses[courseId].completedLessons = Array.from(list);
    storage.setProgress(userId, progress);
}

function getCourseProgressPercent(progress, courseId) {
    const info = progress.courses[courseId];
    if (!info) return 0;
    const course = courses.find(c => c.id === courseId);
    if (!course || course.lessons.length === 0) return 0;
    const pct = Math.round((info.completedLessons.length / course.lessons.length) * 100);
    return Math.min(100, Math.max(0, pct));
}

// --- Auth view (optional) ---
function renderAuth(root) {
    const tpl = document.getElementById('tpl-auth');
    root.innerHTML = '';
    root.appendChild(tpl.content.cloneNode(true));

    const form = document.getElementById('auth-form');
    const email = document.getElementById('auth-email');
    const password = document.getElementById('auth-password');
    const cancel = document.getElementById('cancel-auth');

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const user = { email: email.value.trim(), password: password.value };
        if (!user.email || !user.password) return;
        storage.setUser({ email: user.email }); // Do not store raw password in production
        // Create a progress bucket if not exists
        const existing = storage.getProgress(user.email);
        storage.setProgress(user.email, existing);
        navigateTo('#/');
        wireGlobalNav();
    });
    cancel.addEventListener('click', () => navigateTo('#/'));
}



