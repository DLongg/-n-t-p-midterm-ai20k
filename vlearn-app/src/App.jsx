import React, { useState, useMemo, useEffect } from 'react';
import courseData from './multiphase_course_data.json';
import {
  BookOpen,
  HelpCircle,
  CheckCircle,
  XCircle,
  Lightbulb,
  ChevronRight,
  ChevronLeft,
  Download,
  FileSpreadsheet,
  FileText,
  Award,
  Sparkles,
  RotateCcw,
  Eye,
  Check,
  ExternalLink,
  BookMarked,
  Info,
  CheckSquare,
  CircleDot,
  ArrowUpDown,
  Shuffle,
  Hash,
  Database,
  X,
  Bookmark,
  AlertTriangle,
  Flame,
  PlayCircle,
  CheckCheck,
  Menu,
  MoreVertical,
  Lock,
  LogOut,
  Users,
  Shield,
  UserPlus,
  Trash2
} from 'lucide-react';

// ============================================================================
// CẤU HÌNH TÀI KHOẢN MẶC ĐỊNH & HỖ TRỢ LƯU TRỮ RIÊNG TỪNG NGƯỜI DÙNG
// ============================================================================
const ACCOUNTS_STORAGE_KEY = 'vlearn_accounts_v1';
const CURRENT_USER_STORAGE_KEY = 'vlearn_current_user_v1';

const DEFAULT_ACCOUNTS = [
  {
    username: 'admin',
    password: '123',
    displayName: 'Quản trị viên (Admin)',
    role: 'admin',
    createdAt: '2026-10-01T00:00:00.000Z'
  },
  {
    username: 'user1',
    password: '123',
    displayName: 'Học viên A (user1)',
    role: 'user',
    createdAt: '2026-10-01T00:00:00.000Z'
  },
  {
    username: 'user2',
    password: '123',
    displayName: 'Học viên B (user2)',
    role: 'user',
    createdAt: '2026-10-01T00:00:00.000Z'
  }
];

function loadAccounts() {
  try {
    const raw = localStorage.getItem(ACCOUNTS_STORAGE_KEY);
    const parsed = raw ? JSON.parse(raw) : [];
    if (!Array.isArray(parsed) || parsed.length === 0) {
      localStorage.setItem(ACCOUNTS_STORAGE_KEY, JSON.stringify(DEFAULT_ACCOUNTS));
      return DEFAULT_ACCOUNTS;
    }
    // Đảm bảo tài khoản admin luôn tồn tại
    const hasAdmin = parsed.some(a => a.username.toLowerCase() === 'admin');
    if (!hasAdmin) {
      const merged = [DEFAULT_ACCOUNTS[0], ...parsed];
      localStorage.setItem(ACCOUNTS_STORAGE_KEY, JSON.stringify(merged));
      return merged;
    }
    return parsed;
  } catch {
    return DEFAULT_ACCOUNTS;
  }
}

function getUserStorageKey(username, suffix) {
  const clean = String(username || 'guest').trim().toLowerCase();
  return `vlearn_u_${clean}_${suffix}`;
}

function getUserSummaryStats(username) {
  try {
    const checkedRaw = localStorage.getItem(getUserStorageKey(username, 'checked'));
    const mistakesRaw = localStorage.getItem(getUserStorageKey(username, 'mistakes'));
    const sessionRaw = localStorage.getItem(getUserStorageKey(username, 'session'));
    const checked = checkedRaw ? JSON.parse(checkedRaw) : {};
    const mistakes = mistakesRaw ? JSON.parse(mistakesRaw) : {};
    const session = sessionRaw ? JSON.parse(sessionRaw) : {};

    const totalDone = Object.values(checked).filter(c => c?.isChecked).length;
    const totalCorrect = Object.values(checked).filter(c => c?.isChecked && c?.isCorrect).length;
    const activeWrong = Object.values(mistakes).filter(m => !m?.isMastered).length;
    const lastDay = session.selectedDayId || 'day01';
    const lastPosKey = `${lastDay}__${session.quizBankMode || 'standard'}`;
    const lastQ = (session.questionPositions?.[lastPosKey] ?? 0) + 1;

    return { totalDone, totalCorrect, activeWrong, lastDay, lastQ };
  } catch {
    return { totalDone: 0, totalCorrect: 0, activeWrong: 0, lastDay: 'day01', lastQ: 1 };
  }
}

// ============================================================================
// COMPONENT MÀN HÌNH ĐĂNG NHẬP / ĐĂNG KÝ
// ============================================================================
function AuthScreen({ accounts, onLoginSuccess, onRegisterAccount }) {
  const [mode, setMode] = useState('login'); // 'login' | 'register'
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [displayName, setDisplayName] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    setError('');

    const cleanUser = username.trim().toLowerCase();
    const cleanPass = password.trim();

    if (!cleanUser || !cleanPass) {
      setError('Vui lòng nhập đầy đủ tên đăng nhập và mật khẩu.');
      return;
    }

    if (mode === 'login') {
      const found = accounts.find(
        acc => acc.username.toLowerCase() === cleanUser && acc.password === cleanPass
      );
      // Hỗ trợ mật khẩu admin123 hoặc 123 cho tài khoản admin mặc định
      const isAdminFallback =
        cleanUser === 'admin' && (cleanPass === 'admin123' || cleanPass === '123') &&
        accounts.find(a => a.username.toLowerCase() === 'admin');

      const matchedAccount = found || isAdminFallback;
      if (!matchedAccount) {
        setError('Tên đăng nhập hoặc mật khẩu không chính xác.');
        return;
      }
      onLoginSuccess(matchedAccount);
    } else {
      if (cleanUser.length < 3) {
        setError('Tên đăng nhập phải có ít nhất 3 ký tự.');
        return;
      }
      if (!/^[a-z0-9_.-]+$/.test(cleanUser)) {
        setError('Tên đăng nhập chỉ dùng chữ cái không dấu, số, dấu chấm hoặc gạch dưới.');
        return;
      }
      const exists = accounts.some(acc => acc.username.toLowerCase() === cleanUser);
      if (exists) {
        setError('Tên đăng nhập này đã tồn tại. Vui lòng chọn tên khác.');
        return;
      }
      const newAcc = {
        username: cleanUser,
        password: cleanPass,
        displayName: displayName.trim() || cleanUser,
        role: 'user',
        createdAt: new Date().toISOString()
      };
      onRegisterAccount(newAcc);
      onLoginSuccess(newAcc);
    }
  };

  return (
    <div className="auth-page-wrapper">
      <div className="auth-card">
        <div className="auth-brand-header">
          <div className="brand-badge" style={{ fontSize: '26px', justifyContent: 'center' }}>
            V<span>Learn</span>
          </div>
          <p className="auth-subtitle">Hệ thống ôn tập & luyện đề cá nhân hóa</p>
        </div>

        <div className="auth-tabs">
          <button
            type="button"
            className={`auth-tab-btn ${mode === 'login' ? 'active' : ''}`}
            onClick={() => { setMode('login'); setError(''); }}
          >
            Đăng nhập
          </button>
          <button
            type="button"
            className={`auth-tab-btn ${mode === 'register' ? 'active' : ''}`}
            onClick={() => { setMode('register'); setError(''); }}
          >
            Tạo tài khoản mới
          </button>
        </div>

        <form onSubmit={handleSubmit} className="auth-form">
          {mode === 'register' && (
            <div className="auth-field">
              <label>Tên hiển thị</label>
              <input
                type="text"
                placeholder="VD: Nguyễn Văn A"
                value={displayName}
                onChange={(e) => setDisplayName(e.target.value)}
              />
            </div>
          )}

          <div className="auth-field">
            <label>Tên đăng nhập</label>
            <input
              type="text"
              placeholder="Nhập username..."
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              autoFocus
            />
          </div>

          <div className="auth-field">
            <label>Mật khẩu</label>
            <input
              type="password"
              placeholder="Nhập mật khẩu..."
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>

          {error && (
            <div className="auth-error-box">
              <AlertTriangle size={15} style={{ flexShrink: 0 }} />
              <span>{error}</span>
            </div>
          )}

          <button type="submit" className="btn-primary auth-submit-btn">
            {mode === 'login' ? 'Đăng nhập vào hệ thống' : 'Đăng ký & Bắt đầu học'}
          </button>
        </form>

        <div className="auth-info-footer">
          <p>
            Mỗi tài khoản có <strong>bộ nhớ riêng biệt</strong>: tự động lưu câu đang làm dở theo từng Day và sổ tay câu sai riêng.
          </p>
        </div>
      </div>
    </div>
  );
}

// ============================================================================
// COMPONENT CHÍNH (ROOT APP)
// ============================================================================
export default function App() {
  const [accounts, setAccounts] = useState(() => loadAccounts());
  const [currentUser, setCurrentUser] = useState(() => {
    try {
      const saved = localStorage.getItem(CURRENT_USER_STORAGE_KEY);
      if (!saved) return null;
      const parsed = JSON.parse(saved);
      const latestAcc = loadAccounts().find(
        a => a.username.toLowerCase() === parsed.username?.toLowerCase()
      );
      return latestAcc || null;
    } catch {
      return null;
    }
  });

  const handleLoginSuccess = (account) => {
    const safeUser = {
      username: account.username,
      displayName: account.displayName || account.username,
      role: account.role || 'user'
    };
    setCurrentUser(safeUser);
    try {
      localStorage.setItem(CURRENT_USER_STORAGE_KEY, JSON.stringify(safeUser));
    } catch {}
  };

  const handleLogout = () => {
    setCurrentUser(null);
    try {
      localStorage.removeItem(CURRENT_USER_STORAGE_KEY);
    } catch {}
  };

  const handleRegisterAccount = (newAcc) => {
    setAccounts(prev => {
      const next = [...prev, newAcc];
      try {
        localStorage.setItem(ACCOUNTS_STORAGE_KEY, JSON.stringify(next));
      } catch {}
      return next;
    });
  };

  const handleUpdateAccounts = (nextAccounts) => {
    setAccounts(nextAccounts);
    try {
      localStorage.setItem(ACCOUNTS_STORAGE_KEY, JSON.stringify(nextAccounts));
    } catch {}
  };

  if (!currentUser) {
    return (
      <AuthScreen
        accounts={accounts}
        onLoginSuccess={handleLoginSuccess}
        onRegisterAccount={handleRegisterAccount}
      />
    );
  }

  return (
    <AuthenticatedWorkspace
      key={currentUser.username.toLowerCase()}
      currentUser={currentUser}
      accounts={accounts}
      onUpdateAccounts={handleUpdateAccounts}
      onLogout={handleLogout}
    />
  );
}

// ============================================================================
// WORKSPACE CHO TỪNG TÀI KHOẢN (KHỞI TẠO BỘ NHỚ ĐỘC LẬP THEO USERNAME)
// ============================================================================
function AuthenticatedWorkspace({ currentUser, accounts, onUpdateAccounts, onLogout }) {
  const isAdmin = currentUser?.role === 'admin';
  const username = currentUser.username.toLowerCase();

  // Đọc phiên làm việc đã lưu của riêng tài khoản này
  const initialSession = useMemo(() => {
    try {
      const raw = localStorage.getItem(getUserStorageKey(username, 'session'));
      return raw ? JSON.parse(raw) : {};
    } catch {
      return {};
    }
  }, [username]);

  const [rawPhaseId, setActivePhaseId] = useState(() => {
    if (!isAdmin) return 'phase1';
    return initialSession.activePhaseId === 'phase2' ? 'phase2' : 'phase1';
  });

  const activePhaseId = isAdmin ? rawPhaseId : 'phase1';
  const currentPhase = courseData.phases.find(p => p.id === activePhaseId) || courseData.phases[0];

  const [selectedDayId, setSelectedDayId] = useState(() => {
    const savedDay = initialSession.selectedDayId;
    const validInPhase = currentPhase.days.some(d => d.day_id === savedDay);
    return validInPhase ? savedDay : currentPhase.days[0].day_id;
  });

  const [activeTab, setActiveTab] = useState(() => initialSession.activeTab || 'quiz');
  const [quizBankMode, setQuizBankMode] = useState(() => initialSession.quizBankMode || 'standard');
  const [studyMode, setStudyMode] = useState(() => Boolean(initialSession.studyMode));
  const [filterType, setFilterType] = useState('all');

  // Lưu vị trí câu hỏi đang làm của từng (Day + Chế độ đề)
  const [questionPositions, setQuestionPositions] = useState(() => {
    return initialSession.questionPositions && typeof initialSession.questionPositions === 'object'
      ? initialSession.questionPositions
      : {};
  });

  // Lưu vị trí slide đang xem của từng Day
  const [slidePositions, setSlidePositions] = useState(() => {
    return initialSession.slidePositions && typeof initialSession.slidePositions === 'object'
      ? initialSession.slidePositions
      : {};
  });

  // Modal trạng thái
  const [showGuideModal, setShowGuideModal] = useState(false);
  const [showGridModal, setShowGridModal] = useState(false);
  const [showMoreActions, setShowMoreActions] = useState(false);
  const [showAdminModal, setShowAdminModal] = useState(false);
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  // State tạo tài khoản trong modal Admin
  const [newAccUsername, setNewAccUsername] = useState('');
  const [newAccPassword, setNewAccPassword] = useState('');
  const [newAccDisplay, setNewAccDisplay] = useState('');
  const [newAccRole, setNewAccRole] = useState('user');
  const [adminMsg, setAdminMsg] = useState('');

  // Dữ liệu câu trả lời của riêng user
  const [userAnswers, setUserAnswers] = useState(() => {
    try {
      const saved = localStorage.getItem(getUserStorageKey(username, 'answers'));
      return saved ? JSON.parse(saved) : {};
    } catch {
      return {};
    }
  });

  // Trạng thái chấm câu hỏi của riêng user
  const [checkedState, setCheckedState] = useState(() => {
    try {
      const saved = localStorage.getItem(getUserStorageKey(username, 'checked'));
      return saved ? JSON.parse(saved) : {};
    } catch {
      return {};
    }
  });

  // Sổ tay câu sai của riêng user
  const [mistakeBook, setMistakeBook] = useState(() => {
    try {
      const saved = localStorage.getItem(getUserStorageKey(username, 'mistakes'));
      return saved ? JSON.parse(saved) : {};
    } catch {
      return {};
    }
  });

  const [showHint, setShowHint] = useState({});
  const [showEssaySolution, setShowEssaySolution] = useState({});

  // Đồng bộ tự động sang bộ nhớ riêng của tài khoản hiện tại
  useEffect(() => {
    try {
      localStorage.setItem(getUserStorageKey(username, 'answers'), JSON.stringify(userAnswers));
    } catch {}
  }, [username, userAnswers]);

  useEffect(() => {
    try {
      localStorage.setItem(getUserStorageKey(username, 'checked'), JSON.stringify(checkedState));
    } catch {}
  }, [username, checkedState]);

  useEffect(() => {
    try {
      localStorage.setItem(getUserStorageKey(username, 'mistakes'), JSON.stringify(mistakeBook));
    } catch {}
  }, [username, mistakeBook]);

  useEffect(() => {
    try {
      const sessionPayload = {
        activePhaseId: isAdmin ? activePhaseId : 'phase1',
        selectedDayId,
        activeTab,
        quizBankMode,
        studyMode,
        questionPositions,
        slidePositions
      };
      localStorage.setItem(getUserStorageKey(username, 'session'), JSON.stringify(sessionPayload));
    } catch {}
  }, [username, isAdmin, activePhaseId, selectedDayId, activeTab, quizBankMode, studyMode, questionPositions, slidePositions]);

  const currentDay = currentPhase.days.find(d => d.day_id === selectedDayId) || currentPhase.days[0];

  // Danh sách câu sai của Day hiện tại
  const dayWrongQuestions = useMemo(() => {
    return Object.values(mistakeBook)
      .filter(m => m.dayId === selectedDayId && !m.isMastered && m.question)
      .map(m => m.question);
  }, [mistakeBook, selectedDayId]);

  // Toàn bộ câu sai các Day
  const totalWrongQuestions = useMemo(() => {
    return Object.values(mistakeBook)
      .filter(m => !m.isMastered && m.question)
      .map(m => m.question);
  }, [mistakeBook]);

  // Danh sách câu hỏi theo chế độ
  const allQuestions = useMemo(() => {
    if (quizBankMode === 'wrong') return dayWrongQuestions;
    if (quizBankMode === 'all_wrong') return totalWrongQuestions;
    if (quizBankMode === 'expanded' && currentDay.expanded_questions) return currentDay.expanded_questions;
    if (quizBankMode === 'essay' && currentDay.essay_questions) return currentDay.essay_questions;
    return currentDay.questions || [];
  }, [quizBankMode, dayWrongQuestions, totalWrongQuestions, currentDay]);

  const slides = currentDay.slides || [];

  // Khóa lưu vị trí câu hỏi theo từng (Day + Mode)
  const currentPosKey = quizBankMode === 'all_wrong'
    ? 'all__all_wrong'
    : `${selectedDayId}__${quizBankMode}`;

  const rawSavedQIndex = questionPositions[currentPosKey] ?? 0;
  const currentQIndex = allQuestions.length > 0
    ? Math.min(Math.max(0, rawSavedQIndex), allQuestions.length - 1)
    : 0;

  const setCurrentQIndex = (nextVal) => {
    setQuestionPositions(prev => {
      const currentVal = prev[currentPosKey] ?? 0;
      const resolved = typeof nextVal === 'function' ? nextVal(currentVal) : nextVal;
      const clamped = allQuestions.length > 0
        ? Math.min(Math.max(0, resolved), allQuestions.length - 1)
        : 0;
      return { ...prev, [currentPosKey]: clamped };
    });
  };

  const activeSlideIndex = slides.length > 0
    ? Math.min(Math.max(0, slidePositions[selectedDayId] ?? 0), slides.length - 1)
    : 0;

  const setActiveSlideIndex = (idx) => {
    setSlidePositions(prev => ({ ...prev, [selectedDayId]: idx }));
  };

  // Bộ lọc câu hỏi
  const filteredQuestionIndices = useMemo(() => {
    return allQuestions.map((q, idx) => {
      const qId = q.question_id || `${selectedDayId}_q${idx}`;
      const status = checkedState[qId];
      const mistake = mistakeBook[qId];
      if (filterType === 'correct') return status?.isChecked && status?.isCorrect ? idx : null;
      if (filterType === 'wrong') return status?.isChecked && !status?.isCorrect ? idx : null;
      if (filterType === 'unanswered') return !status?.isChecked ? idx : null;
      if (filterType === 'need_review') {
        return (mistake && !mistake.isMastered) || (status?.isChecked && !status?.isCorrect) || mistake?.isPinned
          ? idx
          : null;
      }
      return idx;
    }).filter(x => x !== null);
  }, [allQuestions, checkedState, filterType, selectedDayId, mistakeBook]);

  const currentQ = allQuestions[currentQIndex] || null;
  const currentSlide = slides[activeSlideIndex] || slides[0] || null;

  // Bỏ câu hỏi khỏi danh sách câu sai
  const handleRemoveFromWrong = (qIdToRemove) => {
    const qId = qIdToRemove || currentQ?.question_id || `${selectedDayId}_q${currentQIndex}`;
    setMistakeBook(prev => {
      const next = { ...prev };
      delete next[qId];
      return next;
    });
    if (quizBankMode === 'wrong' || quizBankMode === 'all_wrong') {
      if (currentQIndex >= allQuestions.length - 1 && currentQIndex > 0) {
        setCurrentQIndex(currentQIndex - 1);
      }
    }
  };

  // Thêm câu vào danh sách câu sai
  const handleAddToWrong = (q, day) => {
    const isEvent = q && (q.nativeEvent || q.target || q.preventDefault);
    const targetQ = (!isEvent && q && q.interaction) ? q : currentQ;
    const targetDay = (!isEvent && day && (day.day_id || day.dayId)) ? day : currentDay;
    const targetDayId = targetDay.day_id || targetDay.dayId || selectedDayId;
    const qId = targetQ?.question_id || `${targetDayId}_q${currentQIndex}`;

    setMistakeBook(prev => ({
      ...prev,
      [qId]: {
        qId,
        dayId: targetDayId,
        dayLabel: targetDay.day_label || targetDay.dayLabel || 'Day',
        dayTitle: targetDay.title || targetDay.dayTitle || '',
        phaseId: activePhaseId,
        question: JSON.parse(JSON.stringify(targetQ)),
        wrongCount: (prev[qId]?.wrongCount || 0) + 1,
        correctCount: prev[qId]?.correctCount || 0,
        lastAttemptAt: new Date().toISOString(),
        isPinned: true,
        isMastered: false
      }
    }));
  };

  // Chuyển Phase (Chặn tài khoản thường vào Phase 2 / Chapter 3)
  const handleSwitchPhase = (phaseId) => {
    if (phaseId === 'phase2' && !isAdmin) {
      alert('Nội dung Phần 2 (Chapter 3 - Track 3) chỉ dành cho tài khoản Admin.');
      return;
    }
    setActivePhaseId(phaseId);
    const targetPhase = courseData.phases.find(p => p.id === phaseId);
    if (targetPhase && targetPhase.days.length > 0) {
      setSelectedDayId(targetPhase.days[0].day_id);
      setQuizBankMode('standard');
      setFilterType('all');
      if (phaseId === 'phase2') {
        setActiveTab('slide');
      }
    }
  };

  // Chọn đáp án
  const handleSelectChoice = (choiceId, isMulti, qIdOverride) => {
    const qId = qIdOverride || currentQ?.question_id || `${selectedDayId}_q${currentQIndex}`;
    if (checkedState[qId]?.isChecked && !studyMode) return;

    if (isMulti) {
      const currentArr = userAnswers[qId] || [];
      if (currentArr.includes(choiceId)) {
        setUserAnswers({ ...userAnswers, [qId]: currentArr.filter(x => x !== choiceId) });
      } else {
        setUserAnswers({ ...userAnswers, [qId]: [...currentArr, choiceId] });
      }
    } else {
      setUserAnswers({ ...userAnswers, [qId]: choiceId });
    }
  };

  // Kiểm tra đáp án & tự động lưu câu sai vào sổ tay riêng
  const handleCheckAnswer = (qOverride, dayOverride) => {
    const isEvent = qOverride && (qOverride.nativeEvent || qOverride.target || qOverride.preventDefault);
    const targetQ = (!isEvent && qOverride && qOverride.interaction) ? qOverride : currentQ;
    const targetDay = (!isEvent && dayOverride && (dayOverride.day_id || dayOverride.dayId)) ? dayOverride : currentDay;
    const targetDayId = targetDay.day_id || targetDay.dayId || selectedDayId;
    const qId = targetQ?.question_id || `${targetDayId}_q${currentQIndex}`;
    const user = userAnswers[qId];

    if (
      user === undefined ||
      user === null ||
      (Array.isArray(user) && user.length === 0) ||
      (typeof user === 'object' && !Array.isArray(user) && Object.keys(user).length === 0)
    ) {
      alert('Vui lòng chọn hoặc nhập câu trả lời trước khi kiểm tra!');
      return;
    }

    const t = targetQ?.interaction?.type;
    const correctAns = targetQ?.correct_answer;
    let isCorrect = false;

    if (t === 'single_select') {
      isCorrect = user === correctAns;
    } else if (t === 'multi_select') {
      if (Array.isArray(user) && Array.isArray(correctAns)) {
        isCorrect = user.length === correctAns.length && user.every(c => correctAns.includes(c));
      }
    } else if (t === 'numeric_input') {
      const uClean = String(user).replace(/[^0-9.-]/g, '').trim();
      const cClean = String(correctAns).replace(/[^0-9.-]/g, '').trim();
      isCorrect = Math.abs(parseFloat(uClean) - parseFloat(cClean)) < 0.05;
    } else if (t === 'matching') {
      if (user && typeof user === 'object' && typeof correctAns === 'object') {
        const leftKeys = Object.keys(correctAns);
        isCorrect = leftKeys.length > 0 && leftKeys.every(lk => user[lk] === correctAns[lk]);
      }
    } else if (t === 'ordering') {
      if (Array.isArray(user) && Array.isArray(correctAns)) {
        isCorrect = user.length === correctAns.length && user.every((it, idx) => it === correctAns[idx]);
      }
    }

    setCheckedState(prev => ({
      ...prev,
      [qId]: { isChecked: true, isCorrect }
    }));

    setMistakeBook(prev => {
      const existing = prev[qId];
      if (!isCorrect) {
        return {
          ...prev,
          [qId]: {
            qId,
            dayId: targetDay.day_id || targetDay.dayId || selectedDayId,
            dayLabel: targetDay.day_label || targetDay.dayLabel || 'Day',
            dayTitle: targetDay.title || targetDay.dayTitle || '',
            phaseId: activePhaseId,
            question: JSON.parse(JSON.stringify(targetQ)),
            wrongCount: (existing?.wrongCount || 0) + 1,
            correctCount: existing?.correctCount || 0,
            lastAttemptAt: new Date().toISOString(),
            isPinned: existing?.isPinned || false,
            isMastered: false
          }
        };
      } else if (existing) {
        const newCorrectCount = (existing.correctCount || 0) + 1;
        return {
          ...prev,
          [qId]: {
            ...existing,
            correctCount: newCorrectCount,
            lastAttemptAt: new Date().toISOString(),
            isMastered: newCorrectCount >= 2
          }
        };
      }
      return prev;
    });
  };

  // Xuất file text tổng hợp câu sai (Chỉ dành cho Admin)
  const handleExportMistakesTxt = () => {
    if (!isAdmin) return;
    const mistakeList = Object.values(mistakeBook);
    if (mistakeList.length === 0) {
      alert('Sổ tay câu sai hiện đang trống!');
      return;
    }

    let content = `===================================================================\n`;
    content += `       VLEARN - SỔ TAY CÂU HAY SAI (${currentUser.username})\n`;
    content += `       Thời gian xuất: ${new Date().toLocaleString('vi-VN')}\n`;
    content += `       Tổng số câu: ${mistakeList.length} câu\n`;
    content += `===================================================================\n\n`;

    mistakeList.forEach((item, idx) => {
      const q = item.question;
      content += `[CÂU ${idx + 1}] ${item.dayLabel}: ${item.dayTitle} · Mã: ${item.qId}\n`;
      content += `Số lần sai: ${item.wrongCount || 0} lần\n\n`;
      content += `ĐỀ BÀI:\n${q?.interaction?.prompt || ''}\n\n`;

      if (q?.interaction?.choices) {
        content += `LỰA CHỌN:\n`;
        q.interaction.choices.forEach((c, cIdx) => {
          const letter = String.fromCharCode(65 + cIdx);
          const isTrue = Array.isArray(q.correct_answer)
            ? q.correct_answer.includes(c.choice_id)
            : q.correct_answer === c.choice_id;
          content += `  [${letter}] ${c.text}${isTrue ? ' <<== [ĐÚNG]' : ''}\n`;
        });
        content += `\n`;
      }
      if (q?.explanation) {
        content += `LỜI GIẢI:\n${q.explanation}\n\n`;
      }
      content += `-------------------------------------------------------------------\n\n`;
    });

    const blob = new Blob([content], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `VLEARN_CAU_SAI_${currentUser.username}_${new Date().toISOString().slice(0, 10)}.txt`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  // Xem đáp án câu hiện tại
  const handleRevealAnswer = () => {
    const qId = currentQ?.question_id || `${selectedDayId}_q${currentQIndex}`;
    const correctAns = currentQ?.correct_answer;

    setUserAnswers(prev => ({ ...prev, [qId]: correctAns }));
    setCheckedState(prev => ({
      ...prev,
      [qId]: { isChecked: true, isCorrect: true, isRevealed: true }
    }));
  };

  // Mở toàn bộ đáp án trong Day
  const handleRevealAllInDay = () => {
    const newAnswers = { ...userAnswers };
    const newChecked = { ...checkedState };
    allQuestions.forEach(q => {
      newAnswers[q.question_id] = q.correct_answer;
      newChecked[q.question_id] = { isChecked: true, isCorrect: true, isRevealed: true };
    });
    setUserAnswers(newAnswers);
    setCheckedState(newChecked);
  };

  // Làm lại Day hiện tại từ đầu
  const handleResetDayQuiz = () => {
    const newAnswers = { ...userAnswers };
    const newChecked = { ...checkedState };
    allQuestions.forEach(q => {
      delete newAnswers[q.question_id];
      delete newChecked[q.question_id];
    });
    setUserAnswers(newAnswers);
    setCheckedState(newChecked);
    setCurrentQIndex(0);
    setFilterType('all');
  };

  // Quản lý tài khoản (Admin)
  const handleAdminAddAccount = (e) => {
    e.preventDefault();
    setAdminMsg('');
    const cleanU = newAccUsername.trim().toLowerCase();
    const cleanP = newAccPassword.trim();
    if (!cleanU || !cleanP) {
      setAdminMsg('Vui lòng nhập tên đăng nhập và mật khẩu.');
      return;
    }
    if (accounts.some(a => a.username.toLowerCase() === cleanU)) {
      setAdminMsg('Tên đăng nhập này đã tồn tại.');
      return;
    }
    const created = {
      username: cleanU,
      password: cleanP,
      displayName: newAccDisplay.trim() || cleanU,
      role: newAccRole,
      createdAt: new Date().toISOString()
    };
    onUpdateAccounts([...accounts, created]);
    setNewAccUsername('');
    setNewAccPassword('');
    setNewAccDisplay('');
    setNewAccRole('user');
    setAdminMsg(`Đã tạo tài khoản "${cleanU}" thành công!`);
  };

  const handleAdminDeleteAccount = (targetUsername) => {
    if (targetUsername.toLowerCase() === 'admin') {
      alert('Không thể xóa tài khoản Admin gốc.');
      return;
    }
    if (!window.confirm(`Xóa tài khoản "${targetUsername}"?`)) return;
    onUpdateAccounts(accounts.filter(a => a.username.toLowerCase() !== targetUsername.toLowerCase()));
  };

  const handleAdminResetUserMemory = (targetUsername) => {
    if (!window.confirm(`Xóa toàn bộ lịch sử làm bài & câu sai của "${targetUsername}"?`)) return;
    try {
      localStorage.removeItem(getUserStorageKey(targetUsername, 'answers'));
      localStorage.removeItem(getUserStorageKey(targetUsername, 'checked'));
      localStorage.removeItem(getUserStorageKey(targetUsername, 'mistakes'));
      localStorage.removeItem(getUserStorageKey(targetUsername, 'session'));
      if (targetUsername.toLowerCase() === username) {
        setUserAnswers({});
        setCheckedState({});
        setMistakeBook({});
        setQuestionPositions({});
      }
      setAdminMsg(`Đã làm mới bộ nhớ của "${targetUsername}".`);
    } catch {}
  };

  const currentQId = currentQ?.question_id || `${selectedDayId}_q${currentQIndex}`;
  const isCurrentInMistakes = Boolean(mistakeBook[currentQId] && !mistakeBook[currentQId].isMastered);
  const currentCheckStatus = checkedState[currentQId] || null;
  const isChecked = studyMode || !!currentCheckStatus?.isChecked;
  const isCorrect = studyMode ? true : !!currentCheckStatus?.isCorrect;
  const userAns = studyMode ? currentQ?.correct_answer : userAnswers[currentQId];
  const isEssayRevealed = Boolean(showEssaySolution[currentQId] || studyMode);

  // Thống kê số câu đúng/sai trong Day hiện tại
  const dayCheckedCount = allQuestions.filter(q => checkedState[q.question_id]?.isChecked).length;
  const dayCorrectCount = allQuestions.filter(q => checkedState[q.question_id]?.isCorrect).length;
  const dayReviewCount = allQuestions.filter((q, i) => {
    const qId = q.question_id || `${selectedDayId}_q${i}`;
    const status = checkedState[qId];
    const m = mistakeBook[qId];
    return (m && !m.isMastered) || (status?.isChecked && !status?.isCorrect) || m?.isPinned;
  }).length;

  // File txt bài giải tương ứng (chỉ dùng khi là Admin)
  const txtFileName = `${currentDay.folder}_QUIZ_CHI_TIET_DAP_AN.txt`;
  const txtFileUrl = `/quiz_txt/${txtFileName}`;

  return (
    <div className="vlearn-wrapper">
      {/* Top Header (Đã tối giản, không lặp nút) */}
      <header className="app-header">
        <div className="brand-section">
          <button
            className="mobile-header-toggle"
            onClick={() => setIsSidebarOpen(true)}
            aria-label="Mở danh sách buổi học"
          >
            <Menu size={20} />
          </button>

          <div className="brand-badge">
            V<span>Learn</span>
          </div>

          <button
            className="mobile-day-indicator"
            onClick={() => setIsSidebarOpen(true)}
          >
            <span>{currentDay.day_label}</span>
            <span style={{ fontSize: '10px', opacity: 0.7 }}>▾</span>
          </button>

          {/* Chuyển Phase trên Desktop */}
          <div className="phase-switcher-container">
            <button
              className={`phase-btn ${activePhaseId === 'phase1' ? 'active' : ''}`}
              onClick={() => handleSwitchPhase('phase1')}
            >
              Phase 1 (Day 1–16)
            </button>
            <button
              className={`phase-btn ${activePhaseId === 'phase2' ? 'active' : ''} ${!isAdmin ? 'locked' : ''}`}
              onClick={() => handleSwitchPhase('phase2')}
              title={!isAdmin ? 'Nội dung Phần 2 (Chapter 3) chỉ dành cho Admin' : 'Phase 2: Track 3 (Day 16 - 29)'}
            >
              {!isAdmin && <Lock size={13} />}
              <span>Phase 2 (Chapter 3)</span>
            </button>
          </div>
        </div>

        {/* Điều hướng trung tâm & Thông tin tài khoản */}
        <div className="header-nav">
          <button
            className={`nav-tab-btn ${activeTab === 'quiz' ? 'active' : ''}`}
            onClick={() => setActiveTab('quiz')}
          >
            <HelpCircle size={16} />
            <span>Quiz ({allQuestions.length})</span>
          </button>

          <button
            className={`nav-tab-btn ${activeTab === 'slide' ? 'active' : ''}`}
            onClick={() => setActiveTab('slide')}
          >
            <BookOpen size={16} />
            <span>Slide ({slides.length})</span>
          </button>

          <button
            className="nav-tab-btn"
            style={{ background: '#f8fafc', border: '1px solid #cbd5e1', color: '#334155' }}
            onClick={() => setShowMoreActions(true)}
          >
            <MoreVertical size={15} />
            <span>Tiện ích</span>
          </button>

          {isAdmin && (
            <button
              className="nav-tab-btn"
              style={{ background: '#eff6ff', border: '1px solid #bfdbfe', color: '#1d4ed8' }}
              onClick={() => { setAdminMsg(''); setShowAdminModal(true); }}
              title="Quản lý danh sách tài khoản & tiến độ"
            >
              <Users size={15} />
              <span>Quản lý TK</span>
            </button>
          )}

          {/* Huy hiệu tài khoản đang đăng nhập */}
          <div className="user-profile-pill">
            <span className={`role-dot ${isAdmin ? 'admin' : 'user'}`} />
            <span className="user-name-text">{currentUser.displayName || currentUser.username}</span>
            <span className={`role-badge-mini ${isAdmin ? 'admin' : 'user'}`}>
              {isAdmin ? 'Admin' : 'User'}
            </span>
            <button
              className="btn-logout-icon"
              onClick={onLogout}
              title="Đăng xuất tài khoản"
            >
              <LogOut size={15} />
            </button>
          </div>
        </div>

        {/* Nút menu phụ trên Mobile */}
        <div className="mobile-right-actions">
          <button
            className="mobile-more-btn"
            onClick={() => setShowMoreActions(true)}
            title="Tiện ích & Tài khoản"
          >
            <MoreVertical size={19} />
          </button>
        </div>
      </header>

      {/* Thanh chuyển Quiz / Slide trên Mobile */}
      <div className="mobile-view-tabs">
        <button
          className={`mobile-view-tab-btn ${activeTab === 'quiz' ? 'active' : ''}`}
          onClick={() => setActiveTab('quiz')}
        >
          <HelpCircle size={15} />
          <span>Quiz ({allQuestions.length})</span>
        </button>
        <button
          className={`mobile-view-tab-btn ${activeTab === 'slide' ? 'active' : ''}`}
          onClick={() => setActiveTab('slide')}
        >
          <BookOpen size={15} />
          <span>Slide ({slides.length})</span>
        </button>
      </div>

      {/* Khung chính */}
      <div className="app-container">
        <div
          className={`sidebar-overlay ${isSidebarOpen ? 'open' : ''}`}
          onClick={() => setIsSidebarOpen(false)}
        />

        {/* Thanh bên danh sách buổi học (Đã loại bỏ chữ lặp 📁 01_Day01) */}
        <aside className={`sidebar ${isSidebarOpen ? 'open' : ''}`}>
          <div className="sidebar-header">
            <div style={{ flex: 1 }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <span className="sidebar-title">
                  {activePhaseId === 'phase1' ? 'Phase 1 · 16 Buổi học' : 'Phase 2 · Chapter 3'}
                </span>
                <button
                  className="sidebar-close-btn"
                  onClick={() => setIsSidebarOpen(false)}
                >
                  <X size={18} />
                </button>
              </div>

              {/* Chuyển Phase trong Drawer Mobile */}
              <div className="mobile-drawer-phase-switch">
                <button
                  className={activePhaseId === 'phase1' ? 'active' : ''}
                  onClick={() => handleSwitchPhase('phase1')}
                >
                  Phase 1
                </button>
                <button
                  className={`${activePhaseId === 'phase2' ? 'active' : ''} ${!isAdmin ? 'locked' : ''}`}
                  onClick={() => handleSwitchPhase('phase2')}
                >
                  {!isAdmin && <Lock size={11} style={{ marginRight: '3px' }} />}
                  Phase 2 (Ch.3)
                </button>
              </div>
            </div>
          </div>

          <div className="sidebar-list">
            {currentPhase.days.map(item => {
              const isSelected = item.day_id === selectedDayId;
              const stdQuestions = item.questions || [];
              const doneInDay = stdQuestions.filter(q => checkedState[q.question_id]?.isChecked).length;
              const dayWrongCount = Object.values(mistakeBook).filter(
                m => m.dayId === item.day_id && !m.isMastered
              ).length;
              const savedIdx = questionPositions[`${item.day_id}__standard`];

              return (
                <button
                  key={item.day_id}
                  className={`day-item-btn ${isSelected ? 'selected' : ''}`}
                  onClick={() => {
                    setSelectedDayId(item.day_id);
                    setFilterType('all');
                    if (quizBankMode === 'wrong' || quizBankMode === 'all_wrong') {
                      setQuizBankMode('standard');
                    }
                    setIsSidebarOpen(false);
                  }}
                >
                  <div className="day-title-row">
                    <span className="day-code-label">
                      {item.day_label}: {item.title}
                    </span>
                  </div>

                  <div className="day-meta-row">
                    {item.quiz_count > 0 ? (
                      <span className="day-badge">
                        {doneInDay > 0 ? `${doneInDay}/${item.quiz_count} đã làm` : `${item.quiz_count} câu`}
                      </span>
                    ) : (
                      <span className="day-badge" style={{ background: '#f1f5f9', color: '#64748b' }}>
                        Thực hành
                      </span>
                    )}

                    {savedIdx > 0 && item.quiz_count > 0 && (
                      <span className="day-badge" style={{ background: '#e0f2fe', color: '#0369a1' }}>
                        Đang ở câu {savedIdx + 1}
                      </span>
                    )}

                    {dayWrongCount > 0 && (
                      <span className="day-badge" style={{ background: '#fee2e2', color: '#b91c1c' }}>
                        🔥 {dayWrongCount} sai
                      </span>
                    )}

                    <span style={{ fontSize: '11px', color: '#94a3b8', marginLeft: 'auto' }}>
                      {item.slides.length} slide
                    </span>
                  </div>
                </button>
              );
            })}
          </div>
        </aside>

        {/* Nội dung chính */}
        <main
          className="main-view-area"
          onContextMenu={(e) => {
            if (!isAdmin && activeTab === 'slide') {
              e.preventDefault();
            }
          }}
        >
          {activeTab === 'slide' ? (
            /* TAB XEM SLIDE BÀI GIẢNG */
            <div className="slide-screen">
              <div className="slide-toolbar">
                <h3 style={{ fontSize: '16px', fontWeight: 700, color: '#0f172a' }}>
                  {currentDay.day_label}: {currentDay.title}
                </h3>

                {/* Chỉ tài khoản Admin mới được tải Slide hoặc mở tab PDF gốc */}
                {currentSlide && isAdmin && (
                  <div className="slide-actions">
                    <a
                      href={currentSlide.url}
                      target="_blank"
                      rel="noreferrer"
                      className="nav-tab-btn"
                    >
                      <ExternalLink size={15} />
                      <span>Mở tab mới</span>
                    </a>
                    <a
                      href={currentSlide.url}
                      target="_blank"
                      rel="noreferrer"
                      className="btn-primary"
                      download
                    >
                      <Download size={15} />
                      <span>Tải PDF</span>
                    </a>
                  </div>
                )}
              </div>

              {slides.length > 1 && (
                <div className="slide-subtabs-row" style={{ padding: '8px 20px' }}>
                  {slides.map((s, idx) => (
                    <button
                      key={idx}
                      className={`slide-subtab-pill ${idx === activeSlideIndex ? 'active' : ''}`}
                      onClick={() => setActiveSlideIndex(idx)}
                    >
                      <FileText size={14} />
                      <span>{s.title || `Slide ${idx + 1}`}</span>
                    </button>
                  ))}
                </div>
              )}

              {currentSlide ? (
                <iframe
                  key={`${currentSlide.url}_${isAdmin ? 'admin' : 'user'}`}
                  src={
                    isAdmin
                      ? `${currentSlide.url}#toolbar=1`
                      : `${currentSlide.url}#toolbar=0&navpanes=0&scrollbar=1`
                  }
                  className="pdf-frame"
                  title="Slide Viewer"
                />
              ) : (
                <div className="q-card" style={{ textAlign: 'center', padding: '48px', margin: '24px' }}>
                  <Award size={48} color="#0284c7" style={{ margin: '0 auto 12px' }} />
                  <h3 style={{ fontSize: '18px', fontWeight: 700 }}>Buổi thực hành / Hackathon</h3>
                  <p style={{ color: '#64748b', fontSize: '14px' }}>
                    Buổi học này không sử dụng slide lý thuyết.
                  </p>
                </div>
              )}
            </div>
          ) : (
            /* TAB LUYỆN QUIZ */
            <div className="quiz-screen">
              {(currentDay.quiz_count > 0 || (currentDay.questions && currentDay.questions.length > 0)) ? (
                <>
                  {/* Khung điều khiển Quiz gọn gàng */}
                  <div className="quiz-header-card">
                    <div className="quiz-controls-top">
                      {/* Chọn nguồn câu hỏi */}
                      <div className="bank-switcher-pills">
                        <button
                          id="btn-bank-standard"
                          className={`bank-pill-btn ${quizBankMode === 'standard' ? 'active-standard' : ''}`}
                          onClick={() => { setQuizBankMode('standard'); setFilterType('all'); }}
                        >
                          🎯 Đề chuẩn ({currentDay.questions?.length || 0})
                        </button>

                        {currentDay.expanded_questions && (
                          <button
                            id="btn-bank-expanded"
                            className={`bank-pill-btn ${quizBankMode === 'expanded' ? 'active-expanded' : ''}`}
                            onClick={() => { setQuizBankMode('expanded'); setFilterType('all'); }}
                          >
                            📚 Kho mở rộng ({currentDay.expanded_questions.length})
                          </button>
                        )}

                        {currentDay.essay_questions && currentDay.essay_questions.length > 0 && (
                          <button
                            id="btn-bank-essay"
                            className={`bank-pill-btn ${quizBankMode === 'essay' ? 'active-essay' : ''}`}
                            onClick={() => { setQuizBankMode('essay'); setFilterType('all'); }}
                          >
                            ✍️ Tự luận ({currentDay.essay_questions.length})
                          </button>
                        )}

                        <button
                          id="btn-day-wrong-questions"
                          className={`bank-pill-btn ${quizBankMode === 'wrong' ? 'active-wrong' : ''}`}
                          onClick={() => { setQuizBankMode('wrong'); setFilterType('all'); }}
                        >
                          <Flame size={13} />
                          <span>Câu sai ({dayWrongQuestions.length})</span>
                        </button>

                        {totalWrongQuestions.length > 0 && (
                          <button
                            id="btn-all-wrong-questions"
                            className={`bank-pill-btn ${quizBankMode === 'all_wrong' ? 'active-all-wrong' : ''}`}
                            onClick={() => { setQuizBankMode('all_wrong'); setFilterType('all'); }}
                          >
                            <AlertTriangle size={13} />
                            <span>Tổng sai ({totalWrongQuestions.length})</span>
                          </button>
                        )}
                      </div>

                      {/* Chế độ Ôn thi (Hiện sẵn đáp án) */}
                      <label className={`study-mode-toggle ${studyMode ? 'active' : ''}`}>
                        <input
                          type="checkbox"
                          checked={studyMode}
                          onChange={(e) => setStudyMode(e.target.checked)}
                        />
                        <BookMarked size={14} />
                        <span>Hiện đáp án</span>
                      </label>
                    </div>

                    {/* Hàng lọc câu hỏi (Không lặp lại dòng chữ Tiến độ bên cạnh) */}
                    <div className="filter-bar-row">
                      <div className="filter-chips-row">
                        {[
                          { id: 'all', label: `Tất cả (${allQuestions.length})` },
                          { id: 'unanswered', label: `Chưa làm (${allQuestions.length - dayCheckedCount})` },
                          { id: 'correct', label: `Đúng (${dayCorrectCount})` },
                          { id: 'wrong', label: `Sai (${dayCheckedCount - dayCorrectCount})` },
                          { id: 'need_review', label: `Cần ôn (${dayReviewCount})` }
                        ].map(f => (
                          <button
                            key={f.id}
                            className={`filter-chip-btn ${filterType === f.id ? 'active' : ''}`}
                            onClick={() => setFilterType(f.id)}
                          >
                            {f.label}
                          </button>
                        ))}
                      </div>
                    </div>

                    {/* Điều hướng câu hỏi rút gọn trên Mobile */}
                    <div className="mobile-nav-summary-row">
                      <button
                        className="nav-step-btn"
                        disabled={currentQIndex === 0}
                        onClick={() => setCurrentQIndex(currentQIndex - 1)}
                      >
                        <ChevronLeft size={16} /> Trước
                      </button>

                      <button
                        className="nav-open-grid-btn"
                        onClick={() => setShowGridModal(true)}
                      >
                        <span className="nav-grid-main">
                          Câu {currentQIndex + 1} / {allQuestions.length}
                        </span>
                        <span className="nav-grid-sub">Bấm chọn câu ▾</span>
                      </button>

                      <button
                        className="nav-step-btn"
                        disabled={currentQIndex === allQuestions.length - 1}
                        onClick={() => setCurrentQIndex(currentQIndex + 1)}
                      >
                        Sau <ChevronRight size={16} />
                      </button>
                    </div>

                    {/* Lưới số thứ tự câu hỏi trên Desktop */}
                    <div className="question-nav-grid desktop-question-nav-grid">
                      {allQuestions.map((q, idx) => {
                        const qId = q.question_id || `${selectedDayId}_q${idx}`;
                        const isAct = idx === currentQIndex;
                        const status = checkedState[qId];

                        let pillClass = '';
                        if (studyMode) {
                          pillClass = 'correct';
                        } else if (status?.isChecked) {
                          pillClass = status.isCorrect ? 'correct' : 'wrong';
                        }

                        const isDimmed = !filteredQuestionIndices.includes(idx);

                        return (
                          <button
                            key={idx}
                            className={`q-nav-pill ${isAct ? 'active' : ''} ${pillClass}`}
                            style={{ opacity: isDimmed ? 0.3 : 1 }}
                            onClick={() => setCurrentQIndex(idx)}
                          >
                            {idx + 1}
                          </button>
                        );
                      })}
                    </div>
                  </div>

                  {/* Trạng thái trống khi không có câu sai */}
                  {(quizBankMode === 'wrong' || quizBankMode === 'all_wrong') && allQuestions.length === 0 && (
                    <div className="q-card" style={{ textAlign: 'center', padding: '44px 24px' }}>
                      <CheckCircle size={36} color="#16a34a" style={{ margin: '0 auto 10px' }} />
                      <h3 style={{ fontSize: '17px', fontWeight: 700, color: '#0f172a' }}>
                        Không có câu sai nào trong danh sách này!
                      </h3>
                      <div style={{ marginTop: '12px' }}>
                        <button
                          id="btn-back-to-standard-quiz"
                          className="btn-primary"
                          onClick={() => setQuizBankMode('standard')}
                        >
                          <PlayCircle size={16} /> Quay lại Đề chuẩn
                        </button>
                      </div>
                    </div>
                  )}

                  {/* THẺ CÂU HỎI HIỆN TẠI (Đã lược bỏ mọi thông báo lặp chữ) */}
                  {currentQ && (
                    <div className="q-card">
                      {/* Hàng thông tin câu hỏi gọn gàng */}
                      <div className="q-badge-row">
                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
                          <span className={`q-type-pill type-${currentQ.interaction?.type || 'single_select'}`}>
                            {currentQ.interaction?.type === 'essay_short_text' ? (
                              <><FileText size={13} /> Tự luận ({currentQ.points || 1}đ)</>
                            ) : currentQ.interaction?.type === 'multi_select' ? (
                              <><CheckSquare size={13} /> Chọn nhiều đáp án</>
                            ) : currentQ.interaction?.type === 'matching' ? (
                              <><Shuffle size={13} /> Ghép cặp</>
                            ) : currentQ.interaction?.type === 'ordering' ? (
                              <><ArrowUpDown size={13} /> Sắp xếp thứ tự</>
                            ) : currentQ.interaction?.type === 'numeric_input' ? (
                              <><Hash size={13} /> Điền số</>
                            ) : (
                              <><CircleDot size={13} /> Chọn 1 đáp án</>
                            )}
                          </span>

                          {currentQ.kc_title && (
                            <span className="q-kc-tag">{currentQ.kc_title}</span>
                          )}

                          {mistakeBook[currentQId]?.wrongCount > 0 && (
                            <span className="q-wrong-count-tag">
                              Sai {mistakeBook[currentQId].wrongCount} lần
                            </span>
                          )}
                        </div>

                        <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginLeft: 'auto' }}>
                          {isCurrentInMistakes ? (
                            <button
                              id="btn-remove-from-wrong"
                              className="btn-mistake-toggle active"
                              onClick={() => handleRemoveFromWrong(currentQId)}
                            >
                              <CheckCheck size={14} />
                              <span>Đã ổn · Bỏ câu sai</span>
                            </button>
                          ) : (
                            <button
                              id="btn-add-to-wrong"
                              className="btn-mistake-toggle"
                              onClick={() => handleAddToWrong(currentQ, currentDay)}
                            >
                              <Bookmark size={13} />
                              <span>Lưu câu sai</span>
                            </button>
                          )}

                          <span className="q-index-meta">
                            Câu {currentQIndex + 1}/{allQuestions.length}
                          </span>
                        </div>
                      </div>

                      {/* Nội dung câu hỏi */}
                      <div className="q-prompt-text">
                        {currentQ.interaction?.prompt}
                      </div>

                      {/* 1. DẠNG TỰ LUẬN (FLASHCARD) */}
                      {currentQ.interaction?.type === 'essay_short_text' && (
                        <div>
                          <button
                            id="btn-toggle-essay-solution"
                            className={`essay-flip-btn ${isEssayRevealed ? 'open' : ''}`}
                            onClick={() => setShowEssaySolution(prev => ({ ...prev, [currentQId]: !isEssayRevealed }))}
                          >
                            <Eye size={17} />
                            <span>
                              {isEssayRevealed ? 'Thu gọn Lời giải & Rubric' : 'Xem Câu trả lời mẫu & Rubric chấm điểm'}
                            </span>
                          </button>

                          {isEssayRevealed && (
                            <div className="essay-solution-stack">
                              {(currentQ.sample_answer || currentQ.explanation) && (
                                <div className="essay-box model-answer">
                                  <div className="essay-box-header">
                                    <Sparkles size={16} />
                                    <span>Câu trả lời mẫu</span>
                                  </div>
                                  <div className="essay-box-body">
                                    {currentQ.sample_answer || currentQ.explanation}
                                  </div>
                                </div>
                              )}

                              {currentQ.rubric && (
                                <div className="essay-box rubric-box">
                                  <div className="essay-box-header">
                                    <CheckSquare size={16} />
                                    <span>Tiêu chí chấm điểm (Rubric)</span>
                                  </div>
                                  <div className="essay-box-body">{currentQ.rubric}</div>
                                </div>
                              )}

                              {(currentQ.reference_source || currentQ.reference || currentQ.source || currentQ.sources) && (
                                <div className="essay-box ref-box">
                                  <div className="essay-box-header">
                                    <BookOpen size={15} />
                                    <span>Tài liệu tham khảo</span>
                                  </div>
                                  <div className="essay-box-body">
                                    {String(currentQ.reference_source || currentQ.reference || currentQ.source || currentQ.sources)}
                                  </div>
                                </div>
                              )}
                            </div>
                          )}
                        </div>
                      )}

                      {/* 2. DẠNG GHÉP CẶP (MATCHING) */}
                      {currentQ.interaction?.type === 'matching' ? (
                        <div className="matching-grid">
                          {currentQ.interaction?.left?.map((lItem, lIdx) => {
                            const userSelected = userAns?.[lItem.id] || '';
                            const trueMatch = currentQ.correct_answer?.[lItem.id];
                            const isPairCorrect = isChecked && userSelected === trueMatch;
                            const rightObj = currentQ.interaction?.right?.find(r => r.id === trueMatch);

                            return (
                              <div
                                key={lIdx}
                                className={`matching-item-card ${isChecked ? (isPairCorrect ? 'correct' : 'wrong') : ''}`}
                              >
                                <div className="matching-item-title">
                                  <span>{lIdx + 1}. {lItem.text}</span>
                                  {isChecked && (
                                    <span className={`pair-status-tag ${isPairCorrect ? 'ok' : 'err'}`}>
                                      {isPairCorrect ? '✓ Đúng' : '✗ Sai'}
                                    </span>
                                  )}
                                </div>
                                <select
                                  className="matching-select"
                                  disabled={isChecked && !studyMode}
                                  value={studyMode ? trueMatch : userSelected}
                                  onChange={(e) => {
                                    const next = { ...(userAns || {}), [lItem.id]: e.target.value };
                                    setUserAnswers({ ...userAnswers, [currentQId]: next });
                                  }}
                                >
                                  <option value="">-- Chọn mệnh đề tương ứng --</option>
                                  {currentQ.interaction?.right?.map((rItem, rIdx) => (
                                    <option key={rIdx} value={rItem.id || rIdx}>
                                      ({String.fromCharCode(65 + rIdx)}) {rItem.text}
                                    </option>
                                  ))}
                                </select>
                                {isChecked && !isPairCorrect && rightObj && (
                                  <div className="matching-correct-hint">
                                    ✓ Đáp án đúng: ({String.fromCharCode(65 + currentQ.interaction.right.findIndex(r => r.id === trueMatch))}) {rightObj.text}
                                  </div>
                                )}
                              </div>
                            );
                          })}
                        </div>
                      ) : currentQ.interaction?.type === 'numeric_input' ? (
                        /* 3. DẠNG ĐIỀN SỐ */
                        <div className="numeric-box">
                          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', flexWrap: 'wrap' }}>
                            <input
                              type="text"
                              className="numeric-input-field"
                              placeholder="Nhập giá trị số..."
                              value={studyMode ? currentQ.correct_answer : (userAns || '')}
                              onChange={(e) => setUserAnswers({ ...userAnswers, [currentQId]: e.target.value })}
                              disabled={isChecked && !studyMode}
                            />
                            {currentQ.interaction?.required_unit && (
                              <span style={{ fontWeight: 600, color: '#64748b' }}>
                                {currentQ.interaction.required_unit}
                              </span>
                            )}
                          </div>
                          {isChecked && (
                            <div style={{ marginTop: '8px', fontSize: '14px', fontWeight: 600, color: isCorrect ? '#059669' : '#dc2626' }}>
                              {isCorrect
                                ? `✓ Chính xác (${currentQ.correct_answer} ${currentQ.interaction?.required_unit || ''})`
                                : `✗ Đáp án đúng: ${currentQ.correct_answer} ${currentQ.interaction?.required_unit || ''}`}
                            </div>
                          )}
                        </div>
                      ) : currentQ.interaction?.type === 'ordering' || currentQ.interaction?.options ? (
                        /* 4. DẠNG SẮP XẾP THỨ TỰ */
                        <div>
                          {(() => {
                            const optionsList = currentQ.interaction?.options || currentQ.interaction?.items || [];
                            const correctOrder = currentQ.correct_answer || [];
                            const orderIds = studyMode
                              ? correctOrder
                              : (Array.isArray(userAns) && userAns.length === optionsList.length
                                  ? userAns
                                  : optionsList.map(o => o.option_id || o.id));

                            const optionsMap = {};
                            optionsList.forEach(o => { optionsMap[o.option_id || o.id] = o.text; });

                            const handleMove = (index, delta) => {
                              if (isChecked && !studyMode) return;
                              const newIdx = index + delta;
                              if (newIdx < 0 || newIdx >= orderIds.length) return;
                              const nextOrder = [...orderIds];
                              const temp = nextOrder[index];
                              nextOrder[index] = nextOrder[newIdx];
                              nextOrder[newIdx] = temp;
                              setUserAnswers({ ...userAnswers, [currentQId]: nextOrder });
                            };

                            return (
                              <div className="ordering-container">
                                {orderIds.map((oid, idx) => {
                                  const isPosCorrect = isChecked && correctOrder[idx] === oid;
                                  return (
                                    <div
                                      key={oid}
                                      className={`ordering-item-row ${isChecked ? (isPosCorrect ? 'correct' : 'wrong') : ''}`}
                                    >
                                      <div style={{ display: 'flex', alignItems: 'center', gap: '12px', flex: 1 }}>
                                        <span className="ordering-step-num">{idx + 1}</span>
                                        <span style={{ fontSize: '14px', color: '#0f172a', fontWeight: 500 }}>
                                          {optionsMap[oid] || oid}
                                        </span>
                                      </div>
                                      {!isChecked && !studyMode && (
                                        <div style={{ display: 'flex', gap: '4px' }}>
                                          <button
                                            disabled={idx === 0}
                                            onClick={() => handleMove(idx, -1)}
                                            className="ordering-move-btn"
                                          >
                                            ↑
                                          </button>
                                          <button
                                            disabled={idx === orderIds.length - 1}
                                            onClick={() => handleMove(idx, 1)}
                                            className="ordering-move-btn"
                                          >
                                            ↓
                                          </button>
                                        </div>
                                      )}
                                    </div>
                                  );
                                })}

                                {isChecked && !isCorrect && Array.isArray(correctOrder) && (
                                  <div className="ordering-solution-box">
                                    <div style={{ fontWeight: 700, color: '#166534', marginBottom: '6px', fontSize: '13px' }}>
                                      ✓ Thứ tự đúng:
                                    </div>
                                    <ol style={{ margin: 0, paddingLeft: '20px', color: '#15803d', fontSize: '13px', lineHeight: 1.6 }}>
                                      {correctOrder.map((coid, cidx) => (
                                        <li key={cidx}>{optionsMap[coid] || coid}</li>
                                      ))}
                                    </ol>
                                  </div>
                                )}
                              </div>
                            );
                          })()}
                        </div>
                      ) : currentQ.interaction?.choices ? (
                        /* 5. DẠNG TRẮC NGHIỆM 1 HOẶC NHIỀU ĐÁP ÁN (Tối giản, không lặp chữ [SAI]) */
                        <div className="choices-container">
                          {currentQ.interaction.choices.map((c, cIdx) => {
                            const letter = String.fromCharCode(65 + cIdx);
                            const isMulti = currentQ.interaction.type === 'multi_select';
                            const isSel = isMulti
                              ? (userAns || []).includes(c.choice_id)
                              : userAns === c.choice_id;

                            const isTrueChoice = isMulti
                              ? (currentQ.correct_answer || []).includes(c.choice_id)
                              : currentQ.correct_answer === c.choice_id;

                            let stateClass = '';
                            let statusLabel = '';

                            if (studyMode) {
                              if (isTrueChoice) {
                                stateClass = 'user-correct';
                                statusLabel = '✓ Đáp án đúng';
                              }
                            } else if (isChecked) {
                              if (isSel && isTrueChoice) {
                                stateClass = 'user-correct';
                                statusLabel = '✓ Đúng';
                              } else if (isSel && !isTrueChoice) {
                                stateClass = 'user-wrong';
                                statusLabel = '✗ Chọn sai';
                              } else if (!isSel && isTrueChoice) {
                                stateClass = 'revealed-correct';
                                statusLabel = '✓ Đáp án đúng';
                              }
                            } else if (isSel) {
                              stateClass = 'selected';
                            }

                            return (
                              <div
                                key={c.choice_id || cIdx}
                                className={`choice-label-card ${stateClass}`}
                                onClick={() => handleSelectChoice(c.choice_id, isMulti)}
                              >
                                <div className="choice-circle">
                                  {isMulti ? (isSel ? '✓' : letter) : letter}
                                </div>
                                <span style={{ fontSize: '15px', color: '#1e293b', fontWeight: 500, flex: 1 }}>
                                  {c.text}
                                </span>
                                {statusLabel && (
                                  <span className={`choice-status-pill ${isTrueChoice ? 'ok' : 'err'}`}>
                                    {statusLabel}
                                  </span>
                                )}
                              </div>
                            );
                          })}
                        </div>
                      ) : null}

                      {/* Gợi ý (nếu có và chưa mở đáp án) */}
                      {currentQ.hints && currentQ.hints.length > 0 && currentQ.interaction?.type !== 'essay_short_text' && !isChecked && (
                        <div>
                          {showHint[currentQId] ? (
                            <div className="hint-box">
                              <Lightbulb size={16} style={{ flexShrink: 0 }} />
                              <div>{currentQ.hints.map(h => h.text).join(' ')}</div>
                            </div>
                          ) : (
                            <button
                              className="btn-hint-link"
                              onClick={() => setShowHint({ ...showHint, [currentQId]: true })}
                            >
                              <Lightbulb size={15} />
                              <span>Xem gợi ý</span>
                            </button>
                          )}
                        </div>
                      )}

                      {/* Hộp giải thích kết quả (Chỉ hiện 1 lần duy nhất) */}
                      {isChecked && currentQ.interaction?.type !== 'essay_short_text' && (
                        <div className={`feedback-box ${isCorrect ? 'correct' : 'incorrect'}`}>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '6px', fontWeight: 700, marginBottom: '4px' }}>
                            {isCorrect ? (
                              <>
                                <CheckCircle size={18} color="#10b981" />
                                <span>Chính xác! Giải thích:</span>
                              </>
                            ) : (
                              <>
                                <XCircle size={18} color="#ef4444" />
                                <span>Chưa chính xác. Giải thích:</span>
                              </>
                            )}
                          </div>
                          <p style={{ fontSize: '14px', lineHeight: 1.6 }}>
                            {currentQ.explanation || currentQ.hints?.[0]?.text || 'Đã đối chiếu theo đáp án chuẩn.'}
                          </p>
                        </div>
                      )}

                      {/* Thanh thao tác dưới thẻ câu hỏi (Desktop) */}
                      <div className="quiz-action-bar desktop-quiz-action-bar">
                        <button
                          className="nav-tab-btn"
                          disabled={currentQIndex === 0}
                          onClick={() => setCurrentQIndex(currentQIndex - 1)}
                        >
                          <ChevronLeft size={16} /> Câu trước
                        </button>

                        <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
                          {!isChecked && !studyMode && currentQ.interaction?.type !== 'essay_short_text' && (
                            <>
                              <button
                                className="nav-tab-btn"
                                style={{ background: '#fef3c7', color: '#92400e', border: '1px solid #fde68a' }}
                                onClick={handleRevealAnswer}
                              >
                                <Eye size={15} /> Xem đáp án
                              </button>

                              <button
                                className="btn-primary"
                                onClick={() => handleCheckAnswer()}
                              >
                                Kiểm tra đáp án
                              </button>
                            </>
                          )}

                          {(isChecked || studyMode || currentQ.interaction?.type === 'essay_short_text') && (
                            <button
                              className="btn-primary"
                              disabled={currentQIndex >= allQuestions.length - 1}
                              onClick={() => {
                                if (currentQIndex < allQuestions.length - 1) {
                                  setCurrentQIndex(currentQIndex + 1);
                                }
                              }}
                            >
                              Câu tiếp theo <ChevronRight size={16} />
                            </button>
                          )}
                        </div>
                      </div>
                    </div>
                  )}
                </>
              ) : (
                /* Trạng thái các buổi không có Quiz */
                <div className="q-card" style={{ textAlign: 'center', padding: '48px' }}>
                  <Award size={48} color="#d97706" style={{ margin: '0 auto 12px' }} />
                  <h3 style={{ fontSize: '18px', fontWeight: 700, color: '#0f172a' }}>
                    {currentDay.day_label}: {currentDay.title}
                  </h3>
                  <p style={{ color: '#64748b', fontSize: '14px', marginTop: '6px' }}>
                    Buổi học này thực hành dự án / Lab, không có bài trắc nghiệm lý thuyết.
                  </p>
                  {slides.length > 0 && (
                    <div style={{ marginTop: '16px' }}>
                      <button
                        className="btn-primary"
                        onClick={() => setActiveTab('slide')}
                      >
                        <BookOpen size={16} /> Chuyển sang xem Slide ({slides.length})
                      </button>
                    </div>
                  )}
                </div>
              )}
            </div>
          )}
        </main>
      </div>

      {/* THANH THAO TÁC CỐ ĐỊNH Ở ĐÁY MÀN HÌNH MOBILE */}
      {activeTab === 'quiz' && currentQ && (
        <div className="mobile-bottom-action-bar">
          <button
            className="mobile-btn-nav"
            disabled={currentQIndex === 0}
            onClick={() => setCurrentQIndex(currentQIndex - 1)}
          >
            <ChevronLeft size={18} />
            <span>Trước</span>
          </button>

          <div className="mobile-bottom-center-cta">
            {currentQ.interaction?.type === 'essay_short_text' ? (
              <button
                className="mobile-btn-cta mobile-btn-essay"
                onClick={() => setShowEssaySolution(prev => ({ ...prev, [currentQId]: !isEssayRevealed }))}
              >
                <Eye size={17} />
                <span>{isEssayRevealed ? 'Thu gọn lời giải' : 'Xem lời giải & Rubric'}</span>
              </button>
            ) : !isChecked && !studyMode ? (
              <div className="mobile-cta-dual">
                <button
                  className="mobile-btn-reveal"
                  onClick={handleRevealAnswer}
                >
                  <Eye size={16} />
                  <span>Đáp án</span>
                </button>
                <button
                  className="mobile-btn-cta mobile-btn-check"
                  onClick={() => handleCheckAnswer()}
                >
                  <Check size={18} />
                  <span>Kiểm tra</span>
                </button>
              </div>
            ) : (
              <button
                className="mobile-btn-cta mobile-btn-next"
                disabled={currentQIndex >= allQuestions.length - 1}
                onClick={() => {
                  if (currentQIndex < allQuestions.length - 1) {
                    setCurrentQIndex(currentQIndex + 1);
                  }
                }}
              >
                <span>Câu tiếp theo</span>
                <ChevronRight size={18} />
              </button>
            )}
          </div>

          <button
            className="mobile-btn-nav"
            disabled={currentQIndex === allQuestions.length - 1}
            onClick={() => setCurrentQIndex(currentQIndex + 1)}
          >
            <ChevronRight size={18} />
            <span>Tiếp</span>
          </button>
        </div>
      )}

      {/* BẢNG CHỌN CÂU HỎI TRÊN MOBILE */}
      {showGridModal && (
        <div className="bottom-sheet-overlay" onClick={() => setShowGridModal(false)}>
          <div className="bottom-sheet-content" onClick={e => e.stopPropagation()}>
            <div className="bottom-sheet-header">
              <div>
                <h3 style={{ fontSize: '16px', fontWeight: 700, color: '#0f172a' }}>
                  Chọn câu hỏi ({allQuestions.length} câu)
                </h3>
              </div>
              <button className="btn-close-sheet" onClick={() => setShowGridModal(false)}>
                <X size={20} />
              </button>
            </div>

            <div className="sheet-grid-container">
              {allQuestions.map((q, idx) => {
                const qId = q.question_id || `${selectedDayId}_q${idx}`;
                const isAct = idx === currentQIndex;
                const status = checkedState[qId];
                let pillClass = '';
                if (studyMode) pillClass = 'correct';
                else if (status?.isChecked) pillClass = status.isCorrect ? 'correct' : 'wrong';

                return (
                  <button
                    key={idx}
                    className={`q-nav-pill ${isAct ? 'active' : ''} ${pillClass}`}
                    onClick={() => {
                      setCurrentQIndex(idx);
                      setShowGridModal(false);
                    }}
                  >
                    {idx + 1}
                  </button>
                );
              })}
            </div>
          </div>
        </div>
      )}

      {/* MENU TIỆN ÍCH & TÀI LIỆU (Phân quyền rõ ràng: User thường không có nút tải) */}
      {showMoreActions && (
        <div className="bottom-sheet-overlay" onClick={() => setShowMoreActions(false)}>
          <div className="bottom-sheet-content more-actions-sheet" onClick={e => e.stopPropagation()}>
            <div className="bottom-sheet-header">
              <div>
                <h3 style={{ fontSize: '16px', fontWeight: 700, color: '#0f172a' }}>
                  Tiện ích & Tài khoản
                </h3>
                <p style={{ fontSize: '12px', color: '#64748b', marginTop: '2px' }}>
                  Đang đăng nhập: <strong>{currentUser.displayName || currentUser.username}</strong> ({isAdmin ? 'Admin' : 'Tài khoản thường'})
                </p>
              </div>
              <button className="btn-close-sheet" onClick={() => setShowMoreActions(false)}>
                <X size={20} />
              </button>
            </div>

            <div className="more-actions-list">
              {/* Xem cấu trúc đề */}
              <button
                className="more-action-item"
                onClick={() => {
                  setShowMoreActions(false);
                  setShowGuideModal(true);
                }}
              >
                <div className="action-icon-wrap" style={{ background: '#e0f2fe', color: '#0369a1' }}>
                  <Info size={18} />
                </div>
                <div className="action-item-info">
                  <span className="action-item-title">Cấu trúc đề thi (5 dạng câu hỏi)</span>
                  <span className="action-item-desc">Giải thích quy tắc chấm điểm của VLearn</span>
                </div>
              </button>

              {/* Hiện tất cả đáp án Day này */}
              {!studyMode && (
                <button
                  className="more-action-item"
                  onClick={() => {
                    handleRevealAllInDay();
                    setShowMoreActions(false);
                  }}
                >
                  <div className="action-icon-wrap" style={{ background: '#eff6ff', color: '#1d4ed8' }}>
                    <Eye size={18} />
                  </div>
                  <div className="action-item-info">
                    <span className="action-item-title">Mở đáp án tất cả câu trong Day này</span>
                    <span className="action-item-desc">Hiển thị đáp án đúng và lời giải cho cả Day</span>
                  </div>
                </button>
              )}

              {/* Làm lại bài thi Day này */}
              {dayCheckedCount > 0 && !studyMode && (
                <button
                  className="more-action-item"
                  onClick={() => {
                    handleResetDayQuiz();
                    setShowMoreActions(false);
                  }}
                >
                  <div className="action-icon-wrap" style={{ background: '#fef2f2', color: '#dc2626' }}>
                    <RotateCcw size={18} />
                  </div>
                  <div className="action-item-info">
                    <span className="action-item-title" style={{ color: '#dc2626' }}>Làm lại Day này từ đầu</span>
                    <span className="action-item-desc">Xóa các câu đã chọn trong {currentDay.day_label} và về Câu 1</span>
                  </div>
                </button>
              )}

              {/* CHỈ ADMIN MỚI ĐƯỢC TẢI CÂU HỎI, SLIDE VÀ FILE XUẤT QUIZ */}
              {isAdmin ? (
                <>
                  <div style={{ fontSize: '11px', fontWeight: 700, color: '#64748b', textTransform: 'uppercase', marginTop: '8px', paddingLeft: '4px' }}>
                    Tải tài liệu & Xuất Quiz (Quyền Admin)
                  </div>

                  <a
                    href="/VLEARN_K4P1_TOAN_BO_QUIZ_VA_SLIDES.xlsx"
                    download
                    className="more-action-item"
                    onClick={() => setShowMoreActions(false)}
                  >
                    <div className="action-icon-wrap" style={{ background: '#dcfce7', color: '#15803d' }}>
                      <FileSpreadsheet size={18} />
                    </div>
                    <div className="action-item-info">
                      <span className="action-item-title">Tải Bảng Excel Master (.xlsx)</span>
                      <span className="action-item-desc">Tổng hợp toàn bộ ngân hàng câu hỏi và đáp án</span>
                    </div>
                  </a>

                  <a
                    href="/TONG_HOP_QUIZ_15_NGAY_EXCEL.zip"
                    download="TONG_HOP_QUIZ_15_NGAY_EXCEL.zip"
                    className="more-action-item"
                    onClick={() => setShowMoreActions(false)}
                  >
                    <div className="action-icon-wrap" style={{ background: '#f3e8ff', color: '#7c3aed' }}>
                      <FileSpreadsheet size={18} />
                    </div>
                    <div className="action-item-info">
                      <span className="action-item-title">Tải Bộ file xuất Quizizz / Quiz.com (.zip)</span>
                      <span className="action-item-desc">45 file Excel chia sẵn ~20 câu/file</span>
                    </div>
                  </a>

                  <a
                    href={`/quiz_excel/Day_${String(currentDay.day_num).padStart(2, '0')}_FULL_TOAN_BO_${currentDay.expanded_questions?.length || currentDay.questions?.length}_CAU.xlsx`}
                    download
                    className="more-action-item"
                    onClick={() => setShowMoreActions(false)}
                  >
                    <div className="action-icon-wrap" style={{ background: '#faf5ff', color: '#7c3aed' }}>
                      <FileSpreadsheet size={18} />
                    </div>
                    <div className="action-item-info">
                      <span className="action-item-title">Xuất Excel Quizizz {currentDay.day_label} (.xlsx)</span>
                      <span className="action-item-desc">File xuất câu hỏi trắc nghiệm của riêng buổi này</span>
                    </div>
                  </a>

                  <a
                    href={txtFileUrl}
                    download={txtFileName}
                    className="more-action-item"
                    onClick={() => setShowMoreActions(false)}
                  >
                    <div className="action-icon-wrap" style={{ background: '#f1f5f9', color: '#334155' }}>
                      <Download size={18} />
                    </div>
                    <div className="action-item-info">
                      <span className="action-item-title">Tải bài giải {currentDay.day_label} (.txt)</span>
                      <span className="action-item-desc">File văn bản đáp án và giải thích chi tiết</span>
                    </div>
                  </a>

                  {currentDay.expanded_txt_url && (
                    <a
                      href={currentDay.expanded_txt_url}
                      download={currentDay.expanded_txt_name || `${currentDay.folder}_NGAN_HANG_TOAN_DIEN.txt`}
                      className="more-action-item"
                      onClick={() => setShowMoreActions(false)}
                    >
                      <div className="action-icon-wrap" style={{ background: '#f5f3ff', color: '#6d28d9' }}>
                        <Database size={18} />
                      </div>
                      <div className="action-item-info">
                        <span className="action-item-title">Tải kho câu hỏi mở rộng (.txt)</span>
                        <span className="action-item-desc">Toàn bộ {currentDay.total_bank_count} câu của buổi này</span>
                      </div>
                    </a>
                  )}

                  <button
                    className="more-action-item"
                    onClick={() => {
                      handleExportMistakesTxt();
                      setShowMoreActions(false);
                    }}
                  >
                    <div className="action-icon-wrap" style={{ background: '#fff1f2', color: '#e11d48' }}>
                      <FileText size={18} />
                    </div>
                    <div className="action-item-info">
                      <span className="action-item-title">Xuất danh sách câu sai (.txt)</span>
                      <span className="action-item-desc">Tải file tổng hợp các câu làm sai của tài khoản này</span>
                    </div>
                  </button>

                  <button
                    className="more-action-item"
                    onClick={() => {
                      setShowMoreActions(false);
                      setAdminMsg('');
                      setShowAdminModal(true);
                    }}
                  >
                    <div className="action-icon-wrap" style={{ background: '#eff6ff', color: '#1d4ed8' }}>
                      <Users size={18} />
                    </div>
                    <div className="action-item-info">
                      <span className="action-item-title">Quản lý danh sách tài khoản</span>
                      <span className="action-item-desc">Thêm/xóa tài khoản và xem tiến độ từng người</span>
                    </div>
                  </button>
                </>
              ) : (
                <div className="restricted-notice-box">
                  <Lock size={15} style={{ flexShrink: 0 }} />
                  <span>
                    Tài khoản thường chỉ hỗ trợ làm bài và xem slide trực tuyến (không tải câu hỏi, slide hoặc xuất file Quiz).
                  </span>
                </div>
              )}

              {/* Nút Đăng xuất */}
              <button
                className="more-action-item"
                onClick={onLogout}
              >
                <div className="action-icon-wrap" style={{ background: '#f1f5f9', color: '#475569' }}>
                  <LogOut size={18} />
                </div>
                <div className="action-item-info">
                  <span className="action-item-title">Đăng xuất ({currentUser.username})</span>
                  <span className="action-item-desc">Chuyển sang tài khoản khác (tiến độ đã được lưu tự động)</span>
                </div>
              </button>
            </div>
          </div>
        </div>
      )}

      {/* MODAL QUẢN LÝ TÀI KHOẢN DÀNH CHO ADMIN */}
      {isAdmin && showAdminModal && (
        <div className="modal-backdrop" onClick={() => setShowAdminModal(false)}>
          <div className="modal-card" onClick={e => e.stopPropagation()} style={{ maxWidth: '680px' }}>
            <div className="modal-header">
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <Shield size={20} color="#0284c7" />
                <h3 style={{ fontSize: '17px', fontWeight: 700 }}>Quản lý Tài khoản & Bộ nhớ riêng</h3>
              </div>
              <button className="btn-close-sheet" onClick={() => setShowAdminModal(false)}>
                <X size={18} />
              </button>
            </div>

            {/* Form thêm tài khoản mới */}
            <form onSubmit={handleAdminAddAccount} className="admin-add-user-form">
              <div style={{ fontSize: '13px', fontWeight: 700, marginBottom: '8px', color: '#0f172a' }}>
                + Tạo tài khoản mới
              </div>
              <div className="admin-form-grid">
                <input
                  type="text"
                  placeholder="Username (VD: user3)"
                  value={newAccUsername}
                  onChange={e => setNewAccUsername(e.target.value)}
                />
                <input
                  type="text"
                  placeholder="Mật khẩu"
                  value={newAccPassword}
                  onChange={e => setNewAccPassword(e.target.value)}
                />
                <input
                  type="text"
                  placeholder="Tên hiển thị"
                  value={newAccDisplay}
                  onChange={e => setNewAccDisplay(e.target.value)}
                />
                <select value={newAccRole} onChange={e => setNewAccRole(e.target.value)}>
                  <option value="user">Tài khoản thường (User)</option>
                  <option value="admin">Quản trị viên (Admin)</option>
                </select>
                <button type="submit" className="btn-primary" style={{ justifyContent: 'center' }}>
                  <UserPlus size={15} /> Thêm
                </button>
              </div>
              {adminMsg && (
                <div style={{ marginTop: '8px', fontSize: '12px', color: '#0369a1', fontWeight: 600 }}>
                  {adminMsg}
                </div>
              )}
            </form>

            {/* Danh sách tài khoản hiện có */}
            <div className="admin-users-list">
              {accounts.map(acc => {
                const stats = getUserSummaryStats(acc.username);
                return (
                  <div key={acc.username} className="admin-user-row">
                    <div>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                        <strong style={{ fontSize: '14px', color: '#0f172a' }}>{acc.displayName || acc.username}</strong>
                        <span style={{ fontSize: '12px', color: '#64748b' }}>@{acc.username}</span>
                        <span className={`role-badge-mini ${acc.role === 'admin' ? 'admin' : 'user'}`}>
                          {acc.role === 'admin' ? 'Admin' : 'User'}
                        </span>
                      </div>
                      <div style={{ fontSize: '12px', color: '#64748b', marginTop: '4px' }}>
                        Đã làm: <strong>{stats.totalDone}</strong> câu ({stats.totalCorrect} đúng) ·
                        Câu sai đang lưu: <strong style={{ color: '#dc2626' }}>{stats.activeWrong}</strong> ·
                        Vị trí gần nhất: <strong>{stats.lastDay.toUpperCase()} - Câu {stats.lastQ}</strong>
                      </div>
                    </div>

                    <div style={{ display: 'flex', gap: '6px' }}>
                      <button
                        type="button"
                        className="admin-action-btn"
                        onClick={() => handleAdminResetUserMemory(acc.username)}
                        title="Xóa lịch sử làm bài của tài khoản này"
                      >
                        <RotateCcw size={14} /> Reset nhớ
                      </button>
                      {acc.username.toLowerCase() !== 'admin' && (
                        <button
                          type="button"
                          className="admin-action-btn danger"
                          onClick={() => handleAdminDeleteAccount(acc.username)}
                          title="Xóa tài khoản"
                        >
                          <Trash2 size={14} />
                        </button>
                      )}
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      )}

      {/* MODAL CẤU TRÚC ĐỀ THI */}
      {showGuideModal && (
        <div className="modal-backdrop" onClick={() => setShowGuideModal(false)}>
          <div className="modal-card" onClick={e => e.stopPropagation()}>
            <div className="modal-header">
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <Info size={20} color="#0284c7" />
                <h3 style={{ fontSize: '17px', fontWeight: 700 }}>Cấu trúc 5 dạng câu hỏi</h3>
              </div>
              <button className="btn-close-sheet" onClick={() => setShowGuideModal(false)}>
                <X size={18} />
              </button>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '10px', fontSize: '13px' }}>
              <div style={{ padding: '10px 12px', borderRadius: '8px', background: '#ecfdf5', border: '1px solid #a7f3d0' }}>
                <strong style={{ color: '#065f46' }}>1. Chọn 1 đáp án:</strong>
                <p style={{ color: '#047857', marginTop: '4px' }}>Chỉ có duy nhất 1 phương án đúng.</p>
              </div>
              <div style={{ padding: '10px 12px', borderRadius: '8px', background: '#eff6ff', border: '1px solid #bfdbfe' }}>
                <strong style={{ color: '#1e40af' }}>2. Chọn nhiều đáp án:</strong>
                <p style={{ color: '#1d4ed8', marginTop: '4px' }}>Tích chọn đầy đủ tất cả các phương án đúng.</p>
              </div>
              <div style={{ padding: '10px 12px', borderRadius: '8px', background: '#faf5ff', border: '1px solid #e9d5ff' }}>
                <strong style={{ color: '#6b21a8' }}>3. Ghép cặp (Matching):</strong>
                <p style={{ color: '#7c3aed', marginTop: '4px' }}>Ghép từng mệnh đề với ý nghĩa tương ứng.</p>
              </div>
              <div style={{ padding: '10px 12px', borderRadius: '8px', background: '#fffbeb', border: '1px solid #fde68a' }}>
                <strong style={{ color: '#92400e' }}>4. Sắp xếp (Ordering):</strong>
                <p style={{ color: '#b45309', marginTop: '4px' }}>Sắp xếp các bước theo đúng trình tự.</p>
              </div>
              <div style={{ padding: '10px 12px', borderRadius: '8px', background: '#fef2f2', border: '1px solid #fecaca' }}>
                <strong style={{ color: '#991b1b' }}>5. Điền số & Tự luận:</strong>
                <p style={{ color: '#b91c1c', marginTop: '4px' }}>Tính toán điền số hoặc đối chiếu Rubric tự luận.</p>
              </div>
            </div>

            <div style={{ textAlign: 'right', marginTop: '16px' }}>
              <button className="btn-primary" onClick={() => setShowGuideModal(false)}>
                Đóng
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
