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
  Layers,
  X,
  Bookmark,
  AlertTriangle,
  Flame,
  Trash2,
  Filter,
  BarChart3,
  Target,
  TrendingUp,
  RefreshCw,
  PlayCircle,
  FileDown,
  Search,
  CheckCheck,
  Menu,
  MoreVertical
} from 'lucide-react';

export default function App() {
  const [activePhaseId, setActivePhaseId] = useState('phase1'); // 'phase1' | 'phase2'
  const currentPhase = courseData.phases.find(p => p.id === activePhaseId) || courseData.phases[0];

  const [selectedDayId, setSelectedDayId] = useState(currentPhase.days[0].day_id);
  const [activeTab, setActiveTab] = useState('quiz'); // 'quiz' | 'slide'
  const [currentQIndex, setCurrentQIndex] = useState(0);
  const [activeSlideIndex, setActiveSlideIndex] = useState(0);

  // Chế độ kho câu hỏi: 'standard' (Đề chuẩn) | 'expanded' (Kho mở rộng) | 'wrong' (Câu hay sai Day này) | 'all_wrong' (Toàn bộ câu sai các Day)
  const [quizBankMode, setQuizBankMode] = useState('standard');

  // Chế độ học tập (Hiện sẵn đáp án và lời giải)
  const [studyMode, setStudyMode] = useState(false);

  // Bộ lọc câu hỏi: 'all' | 'unanswered' | 'correct' | 'wrong' | 'need_review'
  const [filterType, setFilterType] = useState('all');

  // Modal Hướng dẫn cấu trúc đề thi
  const [showGuideModal, setShowGuideModal] = useState(false);

  // Modal/Sheet Lưới câu hỏi trên Mobile
  const [showGridModal, setShowGridModal] = useState(false);

  // Sheet Thao tác khác & Tài liệu tải về trên Mobile
  const [showMoreActions, setShowMoreActions] = useState(false);

  // Trạng thái mở/đóng Sidebar Drawer trên Mobile
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  // Trạng thái câu trả lời người dùng (Tự động nạp từ LocalStorage)
  const [userAnswers, setUserAnswers] = useState(() => {
    try {
      const saved = localStorage.getItem('vlearn_user_answers_v2');
      return saved ? JSON.parse(saved) : {};
    } catch {
      return {};
    }
  });

  const [checkedState, setCheckedState] = useState(() => {
    try {
      const saved = localStorage.getItem('vlearn_checked_state_v2');
      return saved ? JSON.parse(saved) : {};
    } catch {
      return {};
    }
  });

  const [showHint, setShowHint] = useState({});
  const [showEssaySolution, setShowEssaySolution] = useState({});

  // SỔ TAY CÂU HAY SAI (Lưu trữ bền vững trong LocalStorage)
  const [mistakeBook, setMistakeBook] = useState(() => {
    try {
      const saved = localStorage.getItem('vlearn_mistake_book_v2');
      return saved ? JSON.parse(saved) : {};
    } catch {
      return {};
    }
  });

  // Đồng bộ LocalStorage tự động
  useEffect(() => {
    try {
      localStorage.setItem('vlearn_mistake_book_v2', JSON.stringify(mistakeBook));
    } catch (e) {
      console.error(e);
    }
  }, [mistakeBook]);

  useEffect(() => {
    try {
      localStorage.setItem('vlearn_user_answers_v2', JSON.stringify(userAnswers));
    } catch (e) {}
  }, [userAnswers]);

  useEffect(() => {
    try {
      localStorage.setItem('vlearn_checked_state_v2', JSON.stringify(checkedState));
    } catch (e) {}
  }, [checkedState]);

  const currentDay = currentPhase.days.find(d => d.day_id === selectedDayId) || currentPhase.days[0];

  // Danh sách câu hay sai của Day hiện tại (chưa bỏ ra)
  const dayWrongQuestions = useMemo(() => {
    return Object.values(mistakeBook)
      .filter(m => m.dayId === selectedDayId && !m.isMastered && m.question)
      .map(m => m.question);
  }, [mistakeBook, selectedDayId]);

  // Toàn bộ câu hay sai trên tất cả các Day
  const totalWrongQuestions = useMemo(() => {
    return Object.values(mistakeBook)
      .filter(m => !m.isMastered && m.question)
      .map(m => m.question);
  }, [mistakeBook]);

  // Bộ câu hỏi hiển thị cho Quiz theo chế độ lựa chọn
  const allQuestions = useMemo(() => {
    if (quizBankMode === 'wrong') return dayWrongQuestions;
    if (quizBankMode === 'all_wrong') return totalWrongQuestions;
    if (quizBankMode === 'expanded' && currentDay.expanded_questions) return currentDay.expanded_questions;
    if (quizBankMode === 'essay' && currentDay.essay_questions) return currentDay.essay_questions;
    return currentDay.questions || [];
  }, [quizBankMode, dayWrongQuestions, totalWrongQuestions, currentDay]);

  const slides = currentDay.slides || [];

  // Bảo vệ currentQIndex luôn hợp lệ khi đổi kho câu hỏi
  useEffect(() => {
    if (currentQIndex >= allQuestions.length && allQuestions.length > 0) {
      setCurrentQIndex(allQuestions.length - 1);
    }
  }, [allQuestions.length, currentQIndex]);

  // Lọc câu hỏi theo filterType
  const filteredQuestionIndices = useMemo(() => {
    return allQuestions.map((q, idx) => {
      const qId = q.question_id || `${selectedDayId}_q${idx}`;
      const status = checkedState[qId];
      const mistake = mistakeBook[qId];
      if (filterType === 'correct') return status?.isChecked && status?.isCorrect ? idx : null;
      if (filterType === 'wrong') return status?.isChecked && !status?.isCorrect ? idx : null;
      if (filterType === 'unanswered') return !status?.isChecked ? idx : null;
      if (filterType === 'need_review') return (mistake && !mistake.isMastered) || (status?.isChecked && !status?.isCorrect) || mistake?.isPinned ? idx : null;
      return idx;
    }).filter(x => x !== null);
  }, [allQuestions, checkedState, filterType, selectedDayId, mistakeBook]);

  const currentQ = allQuestions[currentQIndex] || null;
  const currentSlide = slides[activeSlideIndex] || slides[0] || null;

  // CƠ CHẾ BỎ RA KHỎI CÂU HAY SAI KHI USER THẤY ỔN CÂU ĐÓ RỒI
  const handleRemoveFromWrong = (qIdToRemove) => {
    const qId = qIdToRemove || currentQ?.question_id || `${selectedDayId}_q${currentQIndex}`;
    setMistakeBook(prev => {
      const next = { ...prev };
      delete next[qId];
      return next;
    });
    // Nếu đang ở mode câu sai và xóa câu, điều chỉnh index
    if (quizBankMode === 'wrong' || quizBankMode === 'all_wrong') {
      if (currentQIndex >= allQuestions.length - 1 && currentQIndex > 0) {
        setCurrentQIndex(currentQIndex - 1);
      }
    }
  };

  // Thêm câu vào danh sách câu hay sai
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

  // Chuyển Phase
  const handleSwitchPhase = (phaseId) => {
    setActivePhaseId(phaseId);
    const targetPhase = courseData.phases.find(p => p.id === phaseId);
    if (targetPhase && targetPhase.days.length > 0) {
      setSelectedDayId(targetPhase.days[0].day_id);
      setCurrentQIndex(0);
      setActiveSlideIndex(0);
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

  // Kiểm tra đáp án (Tự động ghi nhận câu sai vào Sổ tay ôn tập)
  const handleCheckAnswer = (qOverride, dayOverride) => {
    const isEvent = qOverride && (qOverride.nativeEvent || qOverride.target || qOverride.preventDefault);
    const targetQ = (!isEvent && qOverride && qOverride.interaction) ? qOverride : currentQ;
    const targetDay = (!isEvent && dayOverride && (dayOverride.day_id || dayOverride.dayId)) ? dayOverride : currentDay;
    const targetDayId = targetDay.day_id || targetDay.dayId || selectedDayId;
    const qId = targetQ?.question_id || `${targetDayId}_q${currentQIndex}`;
    const user = userAnswers[qId];
    
    if (user === undefined || user === null || (Array.isArray(user) && user.length === 0) || (typeof user === 'object' && !Array.isArray(user) && Object.keys(user).length === 0)) {
      alert("Vui lòng chọn hoặc nhập câu trả lời trước khi bấm kiểm tra!");
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
      [qId]: { isChecked: true, isCorrect: isCorrect }
    }));

    // Tự động cập nhật Sổ tay câu sai (Mistake Book)
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
      } else {
        if (existing) {
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
      }
    });
  };

  // Ghim hoặc bỏ ghim câu hỏi vào Sổ tay câu chưa ổn
  const handleTogglePin = (q, day) => {
    const isEvent = q && (q.nativeEvent || q.target || q.preventDefault);
    const targetQ = (!isEvent && q && q.interaction) ? q : currentQ;
    const targetDay = (!isEvent && day && (day.day_id || day.dayId)) ? day : currentDay;
    const targetDayId = targetDay.day_id || targetDay.dayId || selectedDayId;
    const qId = targetQ?.question_id || `${targetDayId}_q${currentQIndex}`;
    
    setMistakeBook(prev => {
      const existing = prev[qId];
      if (existing) {
        if (existing.isPinned && (!existing.wrongCount || existing.wrongCount === 0)) {
          const next = { ...prev };
          delete next[qId];
          return next;
        }
        return {
          ...prev,
          [qId]: {
            ...existing,
            isPinned: !existing.isPinned
          }
        };
      } else {
        return {
          ...prev,
          [qId]: {
            qId,
            dayId: targetDay.day_id || targetDay.dayId || selectedDayId,
            dayLabel: targetDay.day_label || targetDay.dayLabel || 'Day',
            dayTitle: targetDay.title || targetDay.dayTitle || '',
            phaseId: activePhaseId,
            question: targetQ,
            wrongCount: 0,
            correctCount: 0,
            lastAttemptAt: new Date().toISOString(),
            isPinned: true,
            isMastered: false
          }
        };
      }
    });
  };

  // Đánh dấu đã nắm vững hoặc cần ôn lại
  const handleToggleMastered = (qId) => {
    setMistakeBook(prev => {
      if (!prev[qId]) return prev;
      return {
        ...prev,
        [qId]: {
          ...prev[qId],
          isMastered: !prev[qId].isMastered
        }
      };
    });
  };

  // Xóa 1 câu khỏi sổ tay
  const handleRemoveMistake = (qId) => {
    setMistakeBook(prev => {
      const next = { ...prev };
      delete next[qId];
      return next;
    });
  };

  // Xóa toàn bộ sổ tay câu sai
  const handleClearAllMistakes = () => {
    if (window.confirm("Bạn có chắc chắn muốn làm sạch toàn bộ Sổ tay câu sai không?")) {
      setMistakeBook({});
    }
  };

  // Nạp 4 câu khó mẫu để trải nghiệm ngay
  const handleLoadSampleMistakes = () => {
    const samples = {};
    const p1 = courseData.phases[0];
    if (p1 && p1.days.length > 0) {
      p1.days.forEach(day => {
        (day.questions || []).forEach(q => {
          const t = q.interaction?.type;
          const qId = q.question_id;
          if (t === 'multi_select' && !samples['sample_multi']) {
            samples[qId] = {
              qId,
              dayId: day.day_id,
              dayLabel: day.day_label,
              dayTitle: day.title,
              phaseId: 'phase1',
              question: q,
              wrongCount: 2,
              correctCount: 0,
              lastAttemptAt: new Date().toISOString(),
              isPinned: true,
              isMastered: false
            };
            samples['sample_multi'] = true;
          } else if (t === 'matching' && !samples['sample_matching']) {
            samples[qId] = {
              qId,
              dayId: day.day_id,
              dayLabel: day.day_label,
              dayTitle: day.title,
              phaseId: 'phase1',
              question: q,
              wrongCount: 1,
              correctCount: 0,
              lastAttemptAt: new Date().toISOString(),
              isPinned: false,
              isMastered: false
            };
            samples['sample_matching'] = true;
          } else if (t === 'ordering' && !samples['sample_ordering']) {
            samples[qId] = {
              qId,
              dayId: day.day_id,
              dayLabel: day.day_label,
              dayTitle: day.title,
              phaseId: 'phase1',
              question: q,
              wrongCount: 3,
              correctCount: 1,
              lastAttemptAt: new Date().toISOString(),
              isPinned: true,
              isMastered: false
            };
            samples['sample_ordering'] = true;
          } else if (t === 'single_select' && !samples['sample_single']) {
            samples[qId] = {
              qId,
              dayId: day.day_id,
              dayLabel: day.day_label,
              dayTitle: day.title,
              phaseId: 'phase1',
              question: q,
              wrongCount: 2,
              correctCount: 0,
              lastAttemptAt: new Date().toISOString(),
              isPinned: false,
              isMastered: false
            };
            samples['sample_single'] = true;
          }
        });
      });
      delete samples['sample_multi'];
      delete samples['sample_matching'];
      delete samples['sample_ordering'];
      delete samples['sample_single'];
    }
    setMistakeBook(prev => ({ ...prev, ...samples }));
  };

  // Xuất file text tổng hợp câu sai
  const handleExportMistakesTxt = () => {
    if (allMistakeList.length === 0) {
      alert("Sổ tay câu sai hiện đang trống!");
      return;
    }

    let content = `===================================================================\n`;
    content += `       VLEARN - SỔ TAY CÂU HAY SAI & ÔN TẬP KIẾN THỨC YẾU\n`;
    content += `       Thời gian xuất: ${new Date().toLocaleString('vi-VN')}\n`;
    content += `       Tổng số câu cần ôn: ${allMistakeList.length} câu\n`;
    content += `===================================================================\n\n`;

    allMistakeList.forEach((item, idx) => {
      const q = item.question;
      content += `[CÂU ${idx + 1}] ${item.dayLabel}: ${item.dayTitle} · Mã: ${item.qId}\n`;
      content += `Số lần làm sai: ${item.wrongCount || 0} lần | Trạng thái: ${item.isMastered ? 'Đã nắm vững' : 'Chưa ổn / Cần ôn'}\n`;
      content += `Loại câu hỏi: ${
        q.interaction?.type === 'multi_select' ? 'Trắc nghiệm nhiều đáp án' :
        q.interaction?.type === 'matching' ? 'Ghép cặp tương ứng' :
        q.interaction?.type === 'ordering' ? 'Sắp xếp quy trình' :
        q.interaction?.type === 'numeric_input' ? 'Điền số tính toán' :
        'Trắc nghiệm 1 đáp án'
      }\n\n`;
      content += `ĐỀ BÀI:\n${q.interaction?.prompt || ''}\n\n`;

      if (q.interaction?.choices) {
        content += `CÁC PHƯƠNG ÁN LỰA CHỌN:\n`;
        q.interaction.choices.forEach((c, cIdx) => {
          const letter = String.fromCharCode(65 + cIdx);
          const isCorrect = Array.isArray(q.correct_answer) 
            ? q.correct_answer.includes(c.choice_id)
            : q.correct_answer === c.choice_id;
          content += `  [${letter}] ${c.text} ${isCorrect ? ' <<== [ĐÁP ÁN ĐÚNG]' : ''}\n`;
        });
        content += `\n`;
      }

      if (q.explanation) {
        content += `LỜI GIẢI CHI TIẾT:\n${q.explanation}\n\n`;
      }
      content += `-------------------------------------------------------------------\n\n`;
    });

    const blob = new Blob([content], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `VLEARN_SO_TAY_CAU_HAY_SAI_${new Date().toISOString().slice(0, 10)}.txt`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  // Xem đáp án ngay câu hiện tại (Reveal Answer)
  const handleRevealAnswer = () => {
    const qId = currentQ?.question_id || `${selectedDayId}_q${currentQIndex}`;
    const correctAns = currentQ?.correct_answer;
    
    setUserAnswers(prev => ({
      ...prev,
      [qId]: correctAns
    }));

    setCheckedState(prev => ({
      ...prev,
      [qId]: { isChecked: true, isCorrect: true, isRevealed: true }
    }));
  };

  // Mở tất cả đáp án của Day hiện tại (Reveal All)
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

  // Reset quiz của Day hiện tại
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

  // File txt bài giải tương ứng
  const txtFileName = `${currentDay.folder}_QUIZ_CHI_TIET_DAP_AN.txt`;
  const txtFileUrl = `/quiz_txt/${txtFileName}`;

  // Helper tính chữ cái đáp án cho multi_select
  const getMultiSelectLetters = (q) => {
    if (!q || !q.interaction?.choices || !Array.isArray(q.correct_answer)) return [];
    return q.interaction.choices
      .map((c, idx) => q.correct_answer.includes(c.choice_id) ? String.fromCharCode(65 + idx) : null)
      .filter(Boolean);
  };

  // Helper tính chữ cái đáp án cho single_select
  const getSingleSelectLetter = (q) => {
    if (!q || !q.interaction?.choices) return '';
    const idx = q.interaction.choices.findIndex(c => c.choice_id === q.correct_answer);
    return idx >= 0 ? String.fromCharCode(65 + idx) : '';
  };

  return (
    <div className="vlearn-wrapper">
      {/* Top Header */}
      <header className="app-header">
        <div className="brand-section">
          {/* Mobile Hamburger Button */}
          <button 
            className="mobile-header-toggle" 
            onClick={() => setIsSidebarOpen(true)}
            aria-label="Mở danh sách buổi học"
            title="Danh sách buổi học"
          >
            <Menu size={22} />
          </button>

          <div className="brand-badge">
            V<span>Learn</span>
          </div>

          {/* Quick Day Indicator for Tablet/Mobile */}
          <button 
            className="mobile-day-indicator"
            onClick={() => setIsSidebarOpen(true)}
            title="Bấm để đổi buổi học"
          >
            <span>{currentDay.day_label}</span>
            <span style={{ fontSize: '10px', opacity: 0.7 }}>▾</span>
          </button>

          {/* Phase Switcher Tabs (Desktop) */}
          <div className="phase-switcher-container">
            <button
              className={`phase-btn ${activePhaseId === 'phase1' ? 'active' : ''}`}
              onClick={() => handleSwitchPhase('phase1')}
            >
              Phase 1: Day 1 - 16
            </button>
            <button
              className={`phase-btn ${activePhaseId === 'phase2' ? 'active' : ''}`}
              onClick={() => handleSwitchPhase('phase2')}
            >
              Phase 2: Track 3 (Day 16 - 29)
            </button>
          </div>
        </div>

        {/* Desktop Header Nav */}
        <div className="header-nav">
          <button 
            className={`nav-tab-btn ${activeTab === 'quiz' ? 'active' : ''}`}
            onClick={() => setActiveTab('quiz')}
          >
            <HelpCircle size={18} />
            Luyện tập & Quiz {allQuestions.length > 0 ? `(${allQuestions.length} câu)` : ''}
          </button>
          
          <button 
            className={`nav-tab-btn ${activeTab === 'slide' ? 'active' : ''}`}
            onClick={() => setActiveTab('slide')}
          >
            <BookOpen size={18} />
            Slide Bài giảng gốc ({slides.length} file)
          </button>

          {/* Nút Hướng Dẫn Cấu Trúc Đề */}
          <button 
            className="nav-tab-btn"
            style={{ background: '#f8fafc', border: '1px solid #cbd5e1', color: '#0369a1' }}
            onClick={() => setShowGuideModal(true)}
            title="Xem giải thích cấu trúc 5 dạng câu hỏi và thống kê đề thi"
          >
            <Info size={16} />
            Cấu trúc đề (165 câu)
          </button>

          {/* Nút tải Excel Master */}
          <a 
            href="/VLEARN_K4P1_TOAN_BO_QUIZ_VA_SLIDES.xlsx" 
            download 
            className="btn-excel-download"
            title="Tải bảng tính Excel tổng hợp toàn bộ 165 câu Quiz và Ngân hàng 150 câu Day 1"
          >
            <FileSpreadsheet size={16} />
            Tải Bảng Excel (.xlsx)
          </a>

          {/* Nút tải Trọn Bộ Excel Quizizz / Quiz.com (~20 câu/file) */}
          <a 
            href="/TONG_HOP_QUIZ_15_NGAY_EXCEL.zip" 
            download="TONG_HOP_QUIZ_15_NGAY_EXCEL.zip"
            className="btn-excel-download"
            style={{ background: '#7c3aed', color: '#ffffff', borderColor: '#6d28d9' }}
            title="Tải toàn bộ thư mục Excel 15 Ngày (chia nhỏ ~20 câu/file chuẩn Quizizz / Quiz.com) dạng file nén ZIP"
          >
            <FileSpreadsheet size={16} />
            Bộ Quiz.com / Quizizz (.zip)
          </a>
        </div>

        {/* Mobile More Actions Button */}
        <button 
          className="mobile-more-btn"
          onClick={() => setShowMoreActions(true)}
          title="Tài liệu & Tiện ích khác"
        >
          <MoreVertical size={20} />
        </button>
      </header>

      {/* Mobile View Switcher Tabs (Segmented Control below header) */}
      <div className="mobile-view-tabs">
        <button
          className={`mobile-view-tab-btn ${activeTab === 'quiz' ? 'active' : ''}`}
          onClick={() => setActiveTab('quiz')}
        >
          <HelpCircle size={15} />
          <span>Luyện Quiz ({allQuestions.length})</span>
        </button>
        <button
          className={`mobile-view-tab-btn ${activeTab === 'slide' ? 'active' : ''}`}
          onClick={() => setActiveTab('slide')}
        >
          <BookOpen size={15} />
          <span>Slide Bài giảng ({slides.length})</span>
        </button>
      </div>

      {/* Main Container */}
      <div className="app-container">
        {/* Mobile Backdrop Overlay for Sidebar */}
        <div 
          className={`sidebar-overlay ${isSidebarOpen ? 'open' : ''}`}
          onClick={() => setIsSidebarOpen(false)}
        />

        {/* Left Sidebar (Desktop column & Mobile Drawer) */}
        <aside className={`sidebar ${isSidebarOpen ? 'open' : ''}`}>
          <div className="sidebar-header">
            <div style={{ flex: 1 }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <span className="sidebar-title">{currentPhase.name.split(':')[0]}</span>
                <button 
                  className="sidebar-close-btn"
                  onClick={() => setIsSidebarOpen(false)}
                  title="Đóng danh sách"
                >
                  <X size={20} />
                </button>
              </div>
              <p style={{ fontSize: '11px', color: '#64748b', marginTop: '2px' }}>
                {currentPhase.course_id.toUpperCase()} · {currentPhase.days.length} Buổi học
              </p>

              {/* Phase Switcher inside drawer for Mobile */}
              <div style={{ display: 'flex', gap: '4px', background: '#f1f5f9', padding: '3px', borderRadius: '8px', marginTop: '8px' }}>
                <button
                  style={{
                    flex: 1,
                    padding: '5px 8px',
                    borderRadius: '6px',
                    border: 'none',
                    fontSize: '11px',
                    fontWeight: 700,
                    cursor: 'pointer',
                    background: activePhaseId === 'phase1' ? '#0284c7' : 'transparent',
                    color: activePhaseId === 'phase1' ? '#ffffff' : '#64748b'
                  }}
                  onClick={() => handleSwitchPhase('phase1')}
                >
                  Phase 1 (Day 1-16)
                </button>
                <button
                  style={{
                    flex: 1,
                    padding: '5px 8px',
                    borderRadius: '6px',
                    border: 'none',
                    fontSize: '11px',
                    fontWeight: 700,
                    cursor: 'pointer',
                    background: activePhaseId === 'phase2' ? '#0284c7' : 'transparent',
                    color: activePhaseId === 'phase2' ? '#ffffff' : '#64748b'
                  }}
                  onClick={() => handleSwitchPhase('phase2')}
                >
                  Phase 2 (Track 3)
                </button>
              </div>
            </div>
          </div>

          <div className="sidebar-list">
            {currentPhase.days.map(item => {
              const isSelected = item.day_id === selectedDayId;
              const hasQuiz = item.quiz_count > 0;
              const dayWrongCount = Object.values(mistakeBook).filter(m => m.dayId === item.day_id && !m.isMastered).length;

              return (
                <button
                  key={item.day_id}
                  className={`day-item-btn ${isSelected ? 'selected' : ''}`}
                  onClick={() => {
                    setSelectedDayId(item.day_id);
                    setCurrentQIndex(0);
                    setActiveSlideIndex(0);
                    setQuizBankMode('standard');
                    setFilterType('all');
                    setIsSidebarOpen(false); // Tự động đóng mobile drawer khi chọn Day
                  }}
                >
                  <div className="day-title-row">
                    <span className="day-code-label">
                      {item.day_label}: {item.title}
                    </span>
                    <div style={{ display: 'flex', gap: '4px', alignItems: 'center' }}>
                      {dayWrongCount > 0 && (
                        <span className="day-badge" style={{ background: '#fee2e2', color: '#b91c1c', fontWeight: 800 }}>
                          🔥 {dayWrongCount} sai
                        </span>
                      )}
                      {hasQuiz ? (
                        <span className="day-badge">
                          {item.total_bank_count ? `${item.quiz_count} câu (Kho: ${item.total_bank_count})` : `${item.quiz_count} câu quiz`}
                        </span>
                      ) : item.day_num === 16 || item.day_num === 29 ? (
                        <span className="day-badge" style={{ background: '#fef3c7', color: '#92400e' }}>
                          Hackathon
                        </span>
                      ) : (
                        <span className="day-badge" style={{ background: '#f1f5f9', color: '#475569' }}>
                          Track 3
                        </span>
                      )}
                    </div>
                  </div>
                  <div style={{ display: 'flex', gap: '8px', marginTop: '4px', fontSize: '12px', color: '#64748b' }}>
                    <span>📁 {item.folder}</span>
                    <span>·</span>
                    <span>📑 {item.slides.length} slides</span>
                  </div>
                </button>
              );
            })}
          </div>
        </aside>

        {/* Right Main Content */}
        <main className="main-view-area">
          {activeTab === 'slide' ? (
            /* SLIDE VIEWER TAB */
            <div className="slide-screen">
              <div className="slide-toolbar">
                <div>
                  <h3 style={{ fontSize: '17px', fontWeight: 700, color: '#0f172a' }}>
                    {currentDay.day_label}: {currentDay.title}
                  </h3>
                  <p style={{ fontSize: '13px', color: '#64748b', marginTop: '2px' }}>
                    {slides.length > 0 
                      ? `Có ${slides.length} file slide bài giảng gốc chất lượng cao cho ngày này`
                      : 'Ngày làm bài tập thực hành / Hackathon'}
                  </p>
                </div>
                
                {currentSlide && (
                  <div className="slide-actions" style={{ display: 'flex', gap: '10px' }}>
                    <a 
                      href={currentSlide.url} 
                      target="_blank" 
                      rel="noreferrer" 
                      className="nav-tab-btn"
                    >
                      <ExternalLink size={15} />
                      Mở trong tab mới
                    </a>
                    <a 
                      href={currentSlide.url} 
                      target="_blank" 
                      rel="noreferrer" 
                      className="btn-primary"
                      download
                    >
                      <Download size={16} />
                      Tải slide này (.PDF)
                    </a>
                  </div>
                )}
              </div>

              {/* Multi-slide Subtabs */}
              {slides.length > 1 && (
                <div className="slide-subtabs-row">
                  {slides.map((s, idx) => {
                    const isAct = idx === activeSlideIndex;
                    return (
                      <button
                        key={idx}
                        className={`slide-subtab-pill ${isAct ? 'active' : ''}`}
                        onClick={() => setActiveSlideIndex(idx)}
                      >
                        <FileText size={14} />
                        Slide {idx + 1}: {s.title}
                      </button>
                    );
                  })}
                </div>
              )}

              {currentSlide ? (
                <iframe 
                  key={currentSlide.url}
                  src={`${currentSlide.url}#toolbar=1`} 
                  className="pdf-frame" 
                  title="Slide Viewer"
                />
              ) : (
                <div className="q-card" style={{ textAlign: 'center', padding: '60px' }}>
                  <Award size={56} color="#0284c7" style={{ margin: '0 auto 16px' }} />
                  <h3 style={{ fontSize: '20px', fontWeight: 700 }}>Ngày thi đấu Hackathon / Báo cáo</h3>
                  <p style={{ color: '#64748b', fontSize: '14px', marginTop: '6px' }}>
                    Ngày này là phần thi thực chiến theo nhóm, không sử dụng tài liệu slide lý thuyết.
                  </p>
                </div>
              )}
            </div>
          ) : (
            /* QUIZ PRACTICE TAB */
            <div className="quiz-screen">
              {(currentDay.quiz_count > 0 || (currentDay.questions && currentDay.questions.length > 0)) ? (
                <>
                  {/* Quiz Header Card */}
                  <div className="quiz-header-card">
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '12px' }}>
                      <div style={{ flex: 1, minWidth: '260px' }}>
                        <h2 style={{ fontSize: '18px', fontWeight: 700, color: '#0f172a', marginBottom: '8px' }}>
                          Quiz cuối Day: {currentDay.day_label} - {currentDay.title}
                        </h2>

                        {/* BỘ NÚT CHUYỂN ĐỔI: ĐỀ CHUẨN / KHO MỞ RỘNG / CÂU HAY SAI DAY NÀY (Cuộn ngang) */}
                        <div className="bank-switcher-pills">
                          <button
                            id="btn-bank-standard"
                            className={`bank-pill-btn ${quizBankMode === 'standard' ? 'active-standard' : ''}`}
                            onClick={() => { setQuizBankMode('standard'); setCurrentQIndex(0); setFilterType('all'); }}
                          >
                            🎯 Đề chuẩn ({currentDay.questions?.length || 0} câu)
                          </button>

                          {currentDay.expanded_questions && (
                            <button
                              id="btn-bank-expanded"
                              className={`bank-pill-btn ${quizBankMode === 'expanded' ? 'active-expanded' : ''}`}
                              onClick={() => { setQuizBankMode('expanded'); setCurrentQIndex(0); setFilterType('all'); }}
                              title={`Mở khóa toàn bộ ${currentDay.expanded_questions.length} câu hỏi trắc nghiệm của ${currentDay.day_label}`}
                            >
                              📚 Toàn bộ kho ({currentDay.expanded_questions.length} câu)
                            </button>
                          )}

                          {currentDay.essay_questions && currentDay.essay_questions.length > 0 && (
                            <button
                              id="btn-bank-essay"
                              className={`bank-pill-btn ${quizBankMode === 'essay' ? 'active-essay' : ''}`}
                              onClick={() => { setQuizBankMode('essay'); setCurrentQIndex(0); setFilterType('all'); }}
                              title={`Mở khóa ${currentDay.essay_questions.length} câu hỏi tự luận, phân tích tình huống của ${currentDay.day_label}`}
                            >
                              ✍️ Thẻ tự luận ({currentDay.essay_questions.length} câu)
                            </button>
                          )}

                          <button
                            id="btn-day-wrong-questions"
                            className={`bank-pill-btn ${quizBankMode === 'wrong' ? 'active-wrong' : ''}`}
                            style={{
                              background: quizBankMode === 'wrong' ? '#dc2626' : (dayWrongQuestions.length > 0 ? '#fff1f2' : undefined),
                              color: quizBankMode === 'wrong' ? '#ffffff' : (dayWrongQuestions.length > 0 ? '#b91c1c' : undefined),
                              borderColor: quizBankMode === 'wrong' ? '#dc2626' : (dayWrongQuestions.length > 0 ? '#fecaca' : undefined)
                            }}
                            onClick={() => { setQuizBankMode('wrong'); setCurrentQIndex(0); setFilterType('all'); }}
                            title={`Luyện tập riêng các câu làm sai / chưa ổn của ${currentDay.day_label}`}
                          >
                            <Flame size={14} color={quizBankMode === 'wrong' ? '#ffffff' : '#ef4444'} />
                            🔥 Câu hay sai ({dayWrongQuestions.length})
                          </button>

                          {totalWrongQuestions.length > 0 && (
                            <button
                              id="btn-all-wrong-questions"
                              className={`bank-pill-btn ${quizBankMode === 'all_wrong' ? 'active-all-wrong' : ''}`}
                              onClick={() => { setQuizBankMode('all_wrong'); setCurrentQIndex(0); setFilterType('all'); }}
                              title="Luyện tập gom tất cả câu hay sai từ toàn bộ các Day"
                            >
                              <AlertTriangle size={13} />
                              Tổng câu sai các Day ({totalWrongQuestions.length})
                            </button>
                          )}
                        </div>

                        <p style={{ fontSize: '12px', color: '#64748b', marginTop: '6px' }}>
                          {quizBankMode === 'wrong'
                            ? `🔥 Luyện tập các câu hay sai của ${currentDay.day_label}. Khi đã nắm vững câu nào, bấm "Đã ổn · Bỏ khỏi câu hay sai" để loại khỏi danh sách.`
                            : quizBankMode === 'all_wrong'
                            ? `⚡ Luyện tập gom tất cả các câu làm sai từ toàn bộ các Day (${allQuestions.length} câu).`
                            : quizBankMode === 'expanded'
                            ? `📚 Ngân hàng đề thi mở rộng (${allQuestions.length} câu trắc nghiệm bao phủ toàn bộ kiến thức của ${currentDay.day_label}).`
                            : `🎯 Đề thi chuẩn chính thức từ máy chủ VLearn (${allQuestions.length} câu).`}
                        </p>
                      </div>

                      {/* Header Quick Controls & Action Button */}
                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
                        {/* Toggle Study Mode */}
                        <label 
                          style={{ 
                            display: 'flex', 
                            alignItems: 'center', 
                            gap: '7px', 
                            padding: '6px 12px', 
                            borderRadius: '8px', 
                            background: studyMode ? '#f0fdf4' : '#f8fafc', 
                            border: studyMode ? '1px solid #86efac' : '1px solid #cbd5e1', 
                            cursor: 'pointer',
                            fontSize: '12px',
                            fontWeight: 700,
                            color: studyMode ? '#15803d' : '#475569',
                            whiteSpace: 'nowrap'
                          }}
                        >
                          <input 
                            type="checkbox" 
                            checked={studyMode} 
                            onChange={(e) => setStudyMode(e.target.checked)}
                            style={{ accentColor: '#10b981', cursor: 'pointer' }}
                          />
                          <BookMarked size={15} color={studyMode ? '#10b981' : '#64748b'} />
                          Chế độ Ôn thi
                        </label>

                        {/* Nút Thao tác & Tài liệu mở rộng */}
                        <button
                          className="nav-tab-btn"
                          style={{ 
                            padding: '6px 12px', 
                            fontSize: '12px', 
                            background: '#f1f5f9', 
                            border: '1px solid #cbd5e1', 
                            color: '#0f172a',
                            fontWeight: 700,
                            display: 'inline-flex',
                            alignItems: 'center',
                            gap: '6px'
                          }}
                          onClick={() => setShowMoreActions(true)}
                          title="Tải Excel, file txt bài giải, hiện hết đáp án, làm lại"
                        >
                          <Download size={14} />
                          <span>Tài liệu & Tiện ích ▾</span>
                        </button>
                      </div>
                    </div>

                    {/* Progress Bar & Filter Row */}
                    <div style={{ marginTop: '14px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px', borderTop: '1px solid #f1f5f9', paddingTop: '10px' }}>
                      <div style={{ fontSize: '13px', fontWeight: 600, color: '#0369a1' }}>
                        Tiến độ: {studyMode ? `${allQuestions.length}/${allQuestions.length} (Đang mở toàn bộ)` : `${dayCorrectCount}/${dayCheckedCount} đúng (${dayCheckedCount}/${allQuestions.length} đã làm)`}
                      </div>

                      {/* Filter Buttons */}
                      <div className="filter-chips-row">
                        {[
                          { id: 'all', label: `Tất cả (${allQuestions.length})` },
                          { id: 'correct', label: `Đúng (${dayCorrectCount})` },
                          { id: 'wrong', label: `Sai (${dayCheckedCount - dayCorrectCount})` },
                          { id: 'need_review', label: `Cần ôn (${allQuestions.filter((q, i) => {
                            const qId = q.question_id || `${selectedDayId}_q${i}`;
                            const status = checkedState[qId];
                            const m = mistakeBook[qId];
                            return (m && !m.isMastered) || (status?.isChecked && !status?.isCorrect) || m?.isPinned;
                          }).length})` },
                          { id: 'unanswered', label: `Chưa làm (${allQuestions.length - dayCheckedCount})` }
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

                    {/* Mobile Compact Question Navigation Row */}
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
                        title="Bấm để mở danh sách câu hỏi"
                      >
                        <span className="nav-grid-main">
                          Câu {currentQIndex + 1} / {allQuestions.length}
                        </span>
                        <span className="nav-grid-sub">
                          <Hash size={11} style={{ display: 'inline', verticalAlign: 'middle' }} /> Xem bảng {allQuestions.length} câu ▾
                        </span>
                      </button>

                      <button
                        className="nav-step-btn"
                        disabled={currentQIndex === allQuestions.length - 1}
                        onClick={() => setCurrentQIndex(currentQIndex + 1)}
                      >
                        Sau <ChevronRight size={16} />
                      </button>
                    </div>

                    {/* Desktop Question Navigation Grid */}
                    <div className="question-nav-grid desktop-question-nav-grid" style={{ marginTop: '12px', maxHeight: '180px', overflowY: 'auto', padding: '4px' }}>
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

                        // Kiểm tra xem câu này có nằm trong bộ lọc không
                        const isDimmed = !filteredQuestionIndices.includes(idx);

                        return (
                          <button
                            key={idx}
                            className={`q-nav-pill ${isAct ? 'active' : ''} ${pillClass}`}
                            style={{ opacity: isDimmed ? 0.35 : 1 }}
                            onClick={() => setCurrentQIndex(idx)}
                            title={`Câu ${idx + 1}: ${q.question_id}`}
                          >
                            {idx + 1}
                          </button>
                        );
                      })}
                    </div>
                  </div>

                  {/* Empty state khi không còn câu sai nào trong Day này */}
                  {quizBankMode === 'wrong' && dayWrongQuestions.length === 0 && (
                    <div className="q-card" style={{ textAlign: 'center', padding: '50px 24px', background: '#ffffff', borderRadius: '12px', border: '1px solid #e2e8f0', marginTop: '16px' }}>
                      <div style={{ width: '60px', height: '60px', borderRadius: '50%', background: '#dcfce7', display: 'flex', alignItems: 'center', justifyContent: 'center', margin: '0 auto 16px' }}>
                        <CheckCircle size={32} color="#16a34a" />
                      </div>
                      <h3 style={{ fontSize: '19px', fontWeight: 800, color: '#0f172a' }}>
                        Tuyệt vời! Không có câu sai nào trong {currentDay.day_label}
                      </h3>
                      <p style={{ color: '#64748b', fontSize: '14px', maxWidth: '520px', margin: '8px auto 20px', lineHeight: 1.6 }}>
                        Bạn chưa làm sai câu nào trong ngày này, hoặc đã ôn kỹ và bấm "Đã ổn · Bỏ khỏi câu hay sai" cho toàn bộ các câu!
                      </p>
                      <button
                        id="btn-back-to-standard-quiz"
                        className="btn-primary"
                        onClick={() => { setQuizBankMode('standard'); setCurrentQIndex(0); }}
                        style={{ display: 'inline-flex', alignItems: 'center', gap: '8px', padding: '9px 18px' }}
                      >
                        <PlayCircle size={16} /> Luyện tập Đề chuẩn ({currentDay.questions?.length || 0} câu)
                      </button>
                    </div>
                  )}

                  {/* Empty state khi không còn câu sai nào trong toàn bộ các Day */}
                  {quizBankMode === 'all_wrong' && totalWrongQuestions.length === 0 && (
                    <div className="q-card" style={{ textAlign: 'center', padding: '50px 24px', background: '#ffffff', borderRadius: '12px', border: '1px solid #e2e8f0', marginTop: '16px' }}>
                      <div style={{ width: '60px', height: '60px', borderRadius: '50%', background: '#dcfce7', display: 'flex', alignItems: 'center', justifyContent: 'center', margin: '0 auto 16px' }}>
                        <CheckCircle size={32} color="#16a34a" />
                      </div>
                      <h3 style={{ fontSize: '19px', fontWeight: 800, color: '#0f172a' }}>
                        Tuyệt vời! Bạn không còn câu sai nào trong toàn bộ khoá học!
                      </h3>
                      <button
                        className="btn-primary"
                        onClick={() => { setQuizBankMode('standard'); setCurrentQIndex(0); }}
                        style={{ marginTop: '16px', display: 'inline-flex', alignItems: 'center', gap: '8px' }}
                      >
                        <PlayCircle size={16} /> Quay lại Đề chuẩn ({currentDay.day_label})
                      </button>
                    </div>
                  )}

                  {/* Active Question Card */}
                  {currentQ && (
                    <div className="q-card">
                      {/* Question Format Banner */}
                      <div className="q-badge-row" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                          <span 
                            style={{
                              padding: '4px 10px',
                              borderRadius: '6px',
                              fontSize: '12px',
                              fontWeight: 700,
                              display: 'inline-flex',
                              alignItems: 'center',
                              gap: '6px',
                              background: currentQ.interaction?.type === 'essay_short_text' ? '#ccfbf1' :
                                          currentQ.interaction?.type === 'multi_select' ? '#eff6ff' :
                                          currentQ.interaction?.type === 'matching' ? '#faf5ff' :
                                          currentQ.interaction?.type === 'ordering' ? '#fffbeb' :
                                          currentQ.interaction?.type === 'numeric_input' ? '#fef2f2' : '#ecfdf5',
                              color: currentQ.interaction?.type === 'essay_short_text' ? '#0f766e' :
                                     currentQ.interaction?.type === 'multi_select' ? '#1d4ed8' :
                                     currentQ.interaction?.type === 'matching' ? '#7c3aed' :
                                     currentQ.interaction?.type === 'ordering' ? '#b45309' :
                                     currentQ.interaction?.type === 'numeric_input' ? '#b91c1c' : '#047857',
                              border: `1px solid ${
                                currentQ.interaction?.type === 'essay_short_text' ? '#99f6e4' :
                                currentQ.interaction?.type === 'multi_select' ? '#bfdbfe' :
                                currentQ.interaction?.type === 'matching' ? '#e9d5ff' :
                                currentQ.interaction?.type === 'ordering' ? '#fde68a' :
                                currentQ.interaction?.type === 'numeric_input' ? '#fecaca' : '#a7f3d0'
                              }`
                            }}
                          >
                            {currentQ.interaction?.type === 'essay_short_text' ? <><FileText size={14} /> TỰ LUẬN & PHÂN TÍCH TÌNH HUỐNG ({currentQ.points || 1} ĐIỂM)</> :
                             currentQ.interaction?.type === 'multi_select' ? <><CheckSquare size={14} /> TRẮC NGHIỆM NHIỀU ĐÁP ÁN (CHỌN TẤT CẢ Ý ĐÚNG)</> :
                             currentQ.interaction?.type === 'matching' ? <><Shuffle size={14} /> GHÉP CẶP TƯƠNG ỨNG (MATCHING)</> :
                             currentQ.interaction?.type === 'ordering' ? <><ArrowUpDown size={14} /> SẮP XẾP QUY TRÌNH (ORDERING)</> :
                             currentQ.interaction?.type === 'numeric_input' ? <><Hash size={14} /> TÍNH TOÁN ĐIỀN SỐ</> :
                             <><CircleDot size={14} /> TRẮC NGHIỆM 1 ĐÁP ÁN (CHỈ CHỌN 1)</>}
                          </span>

                          {currentQ.kc_title && (
                            <span style={{ fontSize: '12px', background: '#f1f5f9', color: '#475569', padding: '3px 8px', borderRadius: '4px', fontWeight: 600 }}>
                              {currentQ.kc_title}
                            </span>
                          )}
                        </div>

                        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                          {/* Badge nếu từng làm sai */}
                          {mistakeBook[currentQId]?.wrongCount > 0 && (
                            <span style={{ 
                              fontSize: '11px', 
                              background: '#fee2e2', 
                              color: '#b91c1c', 
                              padding: '3px 8px', 
                              borderRadius: '4px', 
                              fontWeight: 700, 
                              display: 'inline-flex', 
                              alignItems: 'center', 
                              gap: '4px' 
                            }}>
                              <AlertTriangle size={12} /> Từng sai {mistakeBook[currentQId].wrongCount} lần
                            </span>
                          )}

                          {/* CƠ CHẾ BỎ RA KHỎI CÂU HAY SAI KHI USER THẤY ỔN CÂU ĐÓ RỒI */}
                          {isCurrentInMistakes ? (
                            <button
                              id="btn-remove-from-wrong"
                              onClick={() => handleRemoveFromWrong(currentQId)}
                              style={{
                                display: 'inline-flex',
                                alignItems: 'center',
                                gap: '6px',
                                background: '#ecfdf5',
                                color: '#059669',
                                border: '1.5px solid #10b981',
                                padding: '5px 14px',
                                borderRadius: '8px',
                                fontSize: '12px',
                                fontWeight: 700,
                                cursor: 'pointer',
                                transition: 'all 0.15s',
                                boxShadow: '0 1px 2px rgba(16, 185, 129, 0.15)'
                              }}
                              title="Bấm vào đây khi bạn đã nắm vững câu này để bỏ ra khỏi danh sách câu hay sai"
                            >
                              <CheckCheck size={15} color="#059669" />
                              ✅ Đã ổn · Bỏ khỏi câu hay sai
                            </button>
                          ) : (
                            <button
                              id="btn-add-to-wrong"
                              onClick={() => handleAddToWrong(currentQ, currentDay)}
                              style={{
                                display: 'inline-flex',
                                alignItems: 'center',
                                gap: '5px',
                                background: '#f8fafc',
                                color: '#64748b',
                                border: '1px solid #cbd5e1',
                                padding: '5px 10px',
                                borderRadius: '8px',
                                fontSize: '12px',
                                fontWeight: 600,
                                cursor: 'pointer'
                              }}
                              title="Gom câu này vào danh sách câu hay sai để ôn lại"
                            >
                              <Bookmark size={13} />
                              + Gom vào câu hay sai
                            </button>
                          )}

                          <span style={{ fontSize: '13px', color: '#64748b', fontWeight: 500 }}>
                            Câu {currentQIndex + 1} / {allQuestions.length} · Mã: {currentQ.question_id} · Độ khó: {currentQ.estimated_difficulty || 'Vừa'}
                          </span>
                        </div>
                      </div>

                      {/* Hướng dẫn riêng cho dạng nhiều đáp án */}
                      {currentQ.interaction?.type === 'multi_select' && (
                        <div style={{ 
                          margin: '12px 0', 
                          padding: '10px 14px', 
                          borderRadius: '6px', 
                          background: '#eff6ff', 
                          borderLeft: '4px solid #3b82f6', 
                          fontSize: '13px', 
                          color: '#1e40af',
                          display: 'flex',
                          alignItems: 'center',
                          gap: '8px'
                        }}>
                          <Info size={16} style={{ flexShrink: 0 }} />
                          <span>
                            <strong>Lưu ý khảo thí:</strong> Câu hỏi này có <strong>nhiều đáp án đúng</strong>. Bạn phải tích chọn đủ tất cả các ý đúng thì VLearn mới chấm điểm chính xác.
                          </span>
                        </div>
                      )}

                      {/* Question Prompt */}
                      <div className="q-prompt-text" style={{ whiteSpace: 'pre-line', fontSize: '15px', lineHeight: 1.6, marginTop: '12px' }}>
                        {currentQ.interaction?.prompt}
                      </div>

                      
                      {/* DÀNH CHO CÂU HỎI TỰ LUẬN & PHÂN TÍCH TÌNH HUỐNG (FLASHCARD) */}
                      {currentQ.interaction?.type === 'essay_short_text' && (
                        <div style={{ marginTop: '20px' }}>
                          <button
                            id="btn-toggle-essay-solution"
                            onClick={() => setShowEssaySolution(prev => ({ ...prev, [currentQId]: !isEssayRevealed }))}
                            style={{
                              width: '100%',
                              padding: '13px 20px',
                              borderRadius: '10px',
                              background: isEssayRevealed ? '#f0fdf4' : '#f8fafc',
                              border: isEssayRevealed ? '2px solid #10b981' : '2px dashed #94a3b8',
                              color: isEssayRevealed ? '#15803d' : '#334155',
                              fontWeight: 700,
                              fontSize: '14px',
                              cursor: 'pointer',
                              display: 'flex',
                              alignItems: 'center',
                              justifyContent: 'center',
                              gap: '8px',
                              transition: 'all 0.2s',
                              boxShadow: isEssayRevealed ? '0 2px 6px rgba(16, 185, 129, 0.15)' : 'none'
                            }}
                          >
                            <Eye size={18} color={isEssayRevealed ? '#10b981' : '#64748b'} />
                            {isEssayRevealed
                              ? (studyMode ? '📖 Đang mở ở Chế độ học tập (Bấm để thu gọn)' : 'Thu gọn Lời giải, Rubric & Tham khảo')
                              : '💡 Bấm để lật thẻ: Xem Câu trả lời mẫu, Rubric chấm điểm & Nguồn tham khảo'}
                          </button>

                          {isEssayRevealed && (
                            <div style={{ marginTop: '16px', display: 'flex', flexDirection: 'column', gap: '14px' }}>
                              
                              {/* 1. CÂU TRẢ LỜI MẪU CHI TIẾT (MODEL ANSWER) */}
                              {(currentQ.sample_answer || currentQ.explanation) && (
                                <div style={{
                                  padding: '16px 20px',
                                  borderRadius: '10px',
                                  background: '#f0fdf4',
                                  border: '1.5px solid #86efac',
                                  boxShadow: '0 1px 3px rgba(16, 185, 129, 0.08)'
                                }}>
                                  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '10px' }}>
                                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px', fontWeight: 800, fontSize: '14px', color: '#166534' }}>
                                      <Sparkles size={18} color="#16a34a" />
                                      <span>CÂU TRẢ LỜI MẪU CHI TIẾT (MODEL ANSWER):</span>
                                    </div>
                                    <span style={{ fontSize: '12px', background: '#dcfce7', color: '#15803d', padding: '2px 8px', borderRadius: '4px', fontWeight: 700 }}>
                                      Thang điểm: {currentQ.points || 1} điểm
                                    </span>
                                  </div>
                                  <div style={{ whiteSpace: 'pre-line', fontSize: '14px', lineHeight: 1.65, color: '#14532d' }}>
                                    {currentQ.sample_answer || currentQ.explanation}
                                  </div>
                                </div>
                              )}

                              {/* 2. TIÊU CHÍ CHẤM ĐIỂM (SPECIFIC GRADING RUBRIC) */}
                              {currentQ.rubric && (
                                <div style={{
                                  padding: '16px 20px',
                                  borderRadius: '10px',
                                  background: '#eff6ff',
                                  border: '1.5px solid #bfdbfe',
                                  boxShadow: '0 1px 3px rgba(59, 130, 246, 0.08)'
                                }}>
                                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px', fontWeight: 800, fontSize: '14px', marginBottom: '10px', color: '#1e40af' }}>
                                    <CheckSquare size={18} color="#2563eb" />
                                    <span>TIÊU CHÍ CHẤM ĐIỂM CHI TIẾT (GRADING RUBRIC):</span>
                                  </div>
                                  <div style={{ whiteSpace: 'pre-line', fontSize: '14px', lineHeight: 1.65, color: '#1e3a8a' }}>
                                    {currentQ.rubric}
                                  </div>
                                </div>
                              )}

                              {/* 3. NGUỒN THAM KHẢO & TÀI LIỆU KỸ THUẬT QUỐC TẾ (REFERENCE SOURCE) */}
                              {(currentQ.reference_source || currentQ.reference || currentQ.source || currentQ.sources) && (
                                <div style={{
                                  padding: '14px 18px',
                                  borderRadius: '10px',
                                  background: '#f8fafc',
                                  border: '1px solid #cbd5e1',
                                  color: '#334155'
                                }}>
                                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px', fontWeight: 800, fontSize: '13px', marginBottom: '8px', color: '#475569' }}>
                                    <BookOpen size={16} color="#0284c7" />
                                    <span>NGUỒN THAM KHẢO & TÀI LIỆU KỸ THUẬT:</span>
                                  </div>
                                  <div style={{ fontSize: '13px', lineHeight: 1.6, color: '#475569', wordBreak: 'break-word' }}>
                                    {String(currentQ.reference_source || currentQ.reference || currentQ.source || currentQ.sources)}
                                  </div>
                                </div>
                              )}

                              {/* 4. GỢI Ý CỐT LÕI (CORE HINTS) */}
                              {currentQ.hints && currentQ.hints.length > 0 && (
                                <div style={{ padding: '12px 16px', borderRadius: '8px', background: '#fffbeb', border: '1px solid #fde68a', color: '#92400e', fontSize: '13px' }}>
                                  <strong>💡 Gợi ý cốt lõi: </strong> {currentQ.hints.map(h => h.text).join(' ')}
                                </div>
                              )}

                            </div>
                          )}
                        </div>
                      )}

                      {/* TÓM TẮT ĐÁP ÁN ĐÚNG KHI ĐÃ KIỂM TRA HOẶC Ở CHẾ ĐỘ ÔN TẬP */}
                      {isChecked && currentQ.interaction?.type !== 'essay_short_text' && (
                        <div style={{
                          margin: '16px 0',
                          padding: '12px 16px',
                          borderRadius: '8px',
                          background: '#f0fdf4',
                          border: '1px solid #86efac',
                          color: '#166534',
                          fontSize: '14px',
                          fontWeight: 600,
                          display: 'flex',
                          alignItems: 'center',
                          gap: '8px'
                        }}>
                          <CheckCircle size={18} color="#16a34a" style={{ flexShrink: 0 }} />
                          <div>
                            {currentQ.interaction?.type === 'multi_select' ? (
                              <span>
                                <strong>ĐÁP ÁN ĐÚNG CHUẨN XÁC:</strong> Cần chọn cả {getMultiSelectLetters(currentQ).length} phương án: <strong>{getMultiSelectLetters(currentQ).map(l => `[${l}]`).join(', ')}</strong>
                              </span>
                            ) : currentQ.interaction?.type === 'single_select' ? (
                              <span>
                                <strong>ĐÁP ÁN ĐÚNG DUY NHẤT:</strong> Phương án <strong>[{getSingleSelectLetter(currentQ)}]</strong>
                              </span>
                            ) : currentQ.interaction?.type === 'numeric_input' ? (
                              <span>
                                <strong>GIÁ TRỊ ĐIỀN CHUẨN XÁC:</strong> {currentQ.correct_answer} {currentQ.interaction?.required_unit || ''}
                              </span>
                            ) : currentQ.interaction?.type === 'ordering' ? (
                              <span>
                                <strong>THỨ TỰ QUY TRÌNH CHUẨN:</strong> Đã được sắp xếp tự động từ Bước 1 đến Bước N bên dưới.
                              </span>
                            ) : (
                              <span>
                                <strong>KẾT QUẢ GHÉP CẶP CHUẨN:</strong> Đã nối chuẩn xác 100% từng cặp bên dưới.
                              </span>
                            )}
                          </div>
                        </div>
                      )}

                      {/* CHOICES / FORM */}
                      {currentQ.interaction?.type === 'matching' ? (
                        /* MATCHING */
                        <div className="matching-grid">
                          <div style={{ fontSize: '13px', fontWeight: 600, color: '#475569', marginBottom: '8px' }}>
                            Chọn ý nghĩa tương ứng cho từng mệnh đề bên dưới:
                          </div>
                          {currentQ.interaction?.left?.map((lItem, lIdx) => {
                            const userSelected = userAns?.[lItem.id] || '';
                            const trueMatch = currentQ.correct_answer?.[lItem.id];
                            const isPairCorrect = isChecked && userSelected === trueMatch;
                            const rightObj = currentQ.interaction?.right?.find(r => r.id === trueMatch);

                            return (
                              <div key={lIdx} style={{ 
                                marginBottom: '12px', 
                                padding: '12px 14px', 
                                borderRadius: '8px', 
                                border: isChecked ? (isPairCorrect ? '2px solid #10b981' : '2px solid #ef4444') : '1px solid #cbd5e1', 
                                background: isChecked ? (isPairCorrect ? '#ecfdf5' : '#fef2f2') : '#ffffff' 
                              }}>
                                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '8px' }}>
                                  <div style={{ fontWeight: 600, color: '#0f172a', fontSize: '14px' }}>
                                    {lIdx + 1}. {lItem.text}
                                  </div>
                                  {isChecked && (
                                    isPairCorrect ? (
                                      <span style={{ color: '#059669', fontSize: '12px', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '4px' }}>
                                        <CheckCircle size={15} /> ĐÚNG
                                      </span>
                                    ) : (
                                      <span style={{ color: '#dc2626', fontSize: '12px', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '4px' }}>
                                        <XCircle size={15} /> SAI
                                      </span>
                                    )
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
                                  style={{ width: '100%', padding: '10px 12px', borderRadius: '6px', border: '1px solid #cbd5e1', fontSize: '14px', background: isChecked ? '#f8fafc' : '#ffffff' }}
                                >
                                  <option value="">-- Chọn ý nghĩa đối ứng --</option>
                                  {currentQ.interaction?.right?.map((rItem, rIdx) => (
                                    <option key={rIdx} value={rItem.id || rIdx}>
                                      ({String.fromCharCode(65 + rIdx)}) {rItem.text}
                                    </option>
                                  ))}
                                </select>
                                {isChecked && !isPairCorrect && rightObj && (
                                  <div style={{ marginTop: '8px', fontSize: '13px', color: '#047857', fontWeight: 600, background: '#f0fdf4', padding: '6px 10px', borderRadius: '4px', borderLeft: '3px solid #10b981' }}>
                                    ✓ Đáp án đúng phải ghép với: ({String.fromCharCode(65 + currentQ.interaction.right.findIndex(r => r.id === trueMatch))}) {rightObj.text}
                                  </div>
                                )}
                              </div>
                            );
                          })}
                        </div>
                      ) : currentQ.interaction?.type === 'numeric_input' ? (
                        /* NUMERIC INPUT */
                        <div style={{ margin: '16px 0' }}>
                          <label style={{ display: 'block', fontSize: '14px', fontWeight: 600, marginBottom: '8px', color: '#334155' }}>
                            Nhập kết quả tính toán {currentQ.interaction?.required_unit ? `(${currentQ.interaction.required_unit})` : ''}:
                          </label>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                            <input 
                              type="text" 
                              className="numeric-input-field"
                              placeholder="Nhập số..."
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
                          {isChecked && !isCorrect && (
                            <div style={{ marginTop: '10px', fontSize: '14px', color: '#047857', fontWeight: 600 }}>
                              ✓ Đáp án đúng chuẩn xác: {currentQ.correct_answer} {currentQ.interaction?.required_unit || ''}
                            </div>
                          )}
                        </div>
                      ) : currentQ.interaction?.type === 'ordering' || currentQ.interaction?.options ? (
                        /* ORDERING */
                        <div style={{ margin: '16px 0' }}>
                          <div style={{ fontSize: '13px', fontWeight: 600, color: '#475569', marginBottom: '8px' }}>
                            Sắp xếp các bước theo đúng thứ tự:
                          </div>
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
                                      style={{ 
                                        display: 'flex', 
                                        alignItems: 'center', 
                                        justifyContent: 'space-between',
                                        padding: '12px 16px', 
                                        background: isChecked ? (isPosCorrect ? '#ecfdf5' : '#fef2f2') : '#f8fafc', 
                                        border: isChecked ? (isPosCorrect ? '2px solid #10b981' : '2px solid #ef4444') : '1px solid #e2e8f0', 
                                        borderRadius: '8px', 
                                        marginBottom: '8px' 
                                      }}
                                    >
                                      <div style={{ display: 'flex', alignItems: 'center', gap: '12px', flex: 1 }}>
                                        <div style={{ width: '28px', height: '28px', borderRadius: '50%', background: '#0284c7', color: '#fff', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 700, fontSize: '13px' }}>
                                          {idx + 1}
                                        </div>
                                        <span style={{ fontSize: '14px', color: '#0f172a', fontWeight: 500 }}>
                                          {optionsMap[oid] || oid}
                                        </span>
                                      </div>
                                      {!isChecked && !studyMode && (
                                        <div style={{ display: 'flex', gap: '4px' }}>
                                          <button 
                                            disabled={idx === 0}
                                            onClick={() => handleMove(idx, -1)}
                                            style={{ padding: '4px 8px', borderRadius: '4px', border: '1px solid #cbd5e1', background: idx === 0 ? '#f1f5f9' : '#ffffff', cursor: idx === 0 ? 'not-allowed' : 'pointer' }}
                                          >
                                            ↑
                                          </button>
                                          <button 
                                            disabled={idx === orderIds.length - 1}
                                            onClick={() => handleMove(idx, 1)}
                                            style={{ padding: '4px 8px', borderRadius: '4px', border: '1px solid #cbd5e1', background: idx === orderIds.length - 1 ? '#f1f5f9' : '#ffffff', cursor: idx === orderIds.length - 1 ? 'not-allowed' : 'pointer' }}
                                          >
                                            ↓
                                          </button>
                                        </div>
                                      )}
                                    </div>
                                  );
                                })}

                                {isChecked && !isCorrect && Array.isArray(correctOrder) && (
                                  <div style={{ marginTop: '14px', background: '#f0fdf4', border: '1px solid #bbf7d0', borderRadius: '8px', padding: '14px' }}>
                                    <div style={{ fontWeight: 700, color: '#166534', marginBottom: '8px', fontSize: '14px' }}>
                                      ✓ Thứ tự quy trình chuẩn xác 100% từ VLearn:
                                    </div>
                                    <ol style={{ margin: 0, paddingLeft: '20px', color: '#15803d', fontSize: '13px', lineHeight: 1.6 }}>
                                      {correctOrder.map((coid, cidx) => (
                                        <li key={cidx}><strong>Bước {cidx + 1}:</strong> {optionsMap[coid] || coid}</li>
                                      ))}
                                    </ol>
                                  </div>
                                )}
                              </div>
                            );
                          })()}
                        </div>
                      ) : currentQ.interaction?.choices ? (
                        /* SINGLE OR MULTI SELECT */
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

                            // Trạng thái hiển thị đúng/sai sau khi kiểm tra hoặc ở studyMode
                            let stateClass = '';
                            let badgeText = '';

                            if (studyMode) {
                              if (isTrueChoice) {
                                stateClass = 'revealed-correct';
                                badgeText = 'ĐÚNG';
                              } else {
                                badgeText = 'SAI';
                              }
                            } else if (isChecked) {
                              if (isSel && isTrueChoice) {
                                stateClass = 'user-correct';
                                badgeText = 'ĐÚNG';
                              } else if (isSel && !isTrueChoice) {
                                stateClass = 'user-wrong';
                                badgeText = 'SAI';
                              } else if (!isSel && isTrueChoice) {
                                stateClass = 'revealed-correct';
                                badgeText = 'ĐÁP ÁN ĐÚNG';
                              } else {
                                badgeText = 'SAI';
                              }
                            } else if (isSel) {
                              stateClass = 'selected';
                            }

                            return (
                              <div 
                                key={c.choice_id || cIdx}
                                className={`choice-label-card ${stateClass}`}
                                onClick={() => handleSelectChoice(c.choice_id, isMulti)}
                                style={{ position: 'relative' }}
                              >
                                <div className="choice-circle">
                                  {isMulti ? (
                                    <span style={{ fontSize: '12px' }}>{isSel ? '☑' : letter}</span>
                                  ) : (
                                    <span>{letter}</span>
                                  )}
                                </div>
                                <span style={{ fontSize: '15px', color: '#1e293b', fontWeight: 500, flex: 1 }}>
                                  {c.text}
                                </span>
                                {badgeText && (
                                  <span style={{ 
                                    fontSize: '11px', 
                                    fontWeight: 700, 
                                    padding: '3px 8px', 
                                    borderRadius: '4px',
                                    background: badgeText.includes('ĐÚNG') ? '#dcfce7' : '#fee2e2',
                                    color: badgeText.includes('ĐÚNG') ? '#15803d' : '#b91c1c',
                                    marginLeft: '8px'
                                  }}>
                                    [{badgeText}]
                                  </span>
                                )}
                              </div>
                            );
                          })}
                        </div>
                      ) : null}

                      {/* Hint Section */}
                      {currentQ.hints && currentQ.hints.length > 0 && (
                        <div style={{ margin: '16px 0' }}>
                          {showHint[currentQId] || studyMode ? (
                            <div className="hint-box">
                              <Lightbulb size={18} style={{ flexShrink: 0 }} />
                              <div>
                                <strong>Gợi ý từ VLearn: </strong>
                                {currentQ.hints.map(h => h.text).join(' ')}
                              </div>
                            </div>
                          ) : (
                            <button 
                              style={{
                                background: 'none',
                                border: 'none',
                                color: '#d97706',
                                fontWeight: 600,
                                fontSize: '13px',
                                cursor: 'pointer',
                                display: 'flex',
                                alignItems: 'center',
                                gap: '6px'
                              }}
                              onClick={() => setShowHint({ ...showHint, [currentQId]: true })}
                            >
                              <Lightbulb size={16} />
                              Xem gợi ý / nguyên lý giải từ VLearn
                            </button>
                          )}
                        </div>
                      )}

                      {/* Real Verified Feedback Box */}
                      {isChecked && currentQ.interaction?.type !== 'essay_short_text' && (
                        <div className={`feedback-box ${isCorrect ? 'correct' : 'incorrect'}`}>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', fontWeight: 700, marginBottom: '6px' }}>
                            {isCorrect ? (
                              <>
                                <CheckCircle size={20} color="#10b981" />
                                <span>CHÍNH XÁC! Lời giải thích từ máy chủ VLearn:</span>
                              </>
                            ) : (
                              <>
                                <XCircle size={20} color="#ef4444" />
                                <span>CHƯA CHÍNH XÁC! Hãy xem lại phân tích lời giải:</span>
                              </>
                            )}
                          </div>
                          
                          <p style={{ fontSize: '14px', marginTop: '8px', lineHeight: 1.6 }}>
                            {currentQ.explanation || currentQ.hints?.[0]?.text || 'Lời giải chi tiết chuẩn xác theo logic chấm điểm của VLearn.'}
                          </p>
                        </div>
                      )}

                      {/* Actions Bottom Bar (Desktop view) */}
                      <div className="quiz-action-bar desktop-quiz-action-bar">
                        <button
                          className="nav-tab-btn"
                          disabled={currentQIndex === 0}
                          onClick={() => setCurrentQIndex(currentQIndex - 1)}
                        >
                          <ChevronLeft size={16} /> Câu trước
                        </button>

                        <div style={{ display: 'flex', gap: '8px', alignItems: 'center', flexWrap: 'wrap' }}>
                          {/* Nút Đã ổn câu này · Bỏ ra ở thanh thao tác cuối */}
                          {isCurrentInMistakes && (
                            <button 
                              id="btn-bottom-remove-wrong"
                              className="nav-tab-btn"
                              style={{ 
                                background: '#ecfdf5', 
                                color: '#059669', 
                                border: '1.5px solid #10b981',
                                fontWeight: 700,
                                display: 'inline-flex',
                                alignItems: 'center',
                                gap: '6px'
                              }}
                              onClick={() => handleRemoveFromWrong(currentQId)}
                              title="Bạn đã thấy ổn câu này rồi? Bấm để bỏ ra khỏi danh sách câu sai"
                            >
                              <CheckCheck size={16} color="#059669" />
                              Đã ổn câu này · Bỏ ra
                            </button>
                          )}
                          {/* Dành cho câu trắc nghiệm / matching / ordering / numeric khi chưa kiểm tra */}
                          {!isChecked && !studyMode && currentQ.interaction?.type !== 'essay_short_text' && (
                            <>
                              <button 
                                className="nav-tab-btn"
                                style={{ background: '#fef3c7', color: '#92400e', border: '1px solid #fde68a' }}
                                onClick={handleRevealAnswer}
                                title="Xem ngay đáp án đúng và lời giải câu này"
                              >
                                <Eye size={16} /> Xem đáp án câu này
                              </button>
                              
                              <button 
                                className="btn-primary"
                                onClick={() => handleCheckAnswer()}
                              >
                                Kiểm tra đáp án
                              </button>
                            </>
                          )}

                          {/* Dành cho câu tự luận ở thanh thao tác Desktop */}
                          {currentQ.interaction?.type === 'essay_short_text' && (
                            <button
                              id="btn-bottom-essay-toggle"
                              className="btn-primary"
                              style={{ background: isEssayRevealed ? '#0d9488' : '#0284c7' }}
                              onClick={() => setShowEssaySolution(prev => ({ ...prev, [currentQId]: !isEssayRevealed }))}
                            >
                              <Eye size={16} />
                              {isEssayRevealed ? 'Thu gọn Lời giải & Rubric' : 'Xem Lời giải & Rubric'}
                            </button>
                          )}

                          {(isChecked || studyMode || currentQ.interaction?.type === 'essay_short_text') && (
                            <button 
                              className="btn-primary"
                              style={{ background: '#0284c7' }}
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
                /* EMPTY STATE FOR DAYS WITHOUT QUIZ */
                <div className="q-card" style={{ textAlign: 'center', padding: '60px' }}>
                  <Award size={56} color="#d97706" style={{ margin: '0 auto 16px' }} />
                  <h3 style={{ fontSize: '20px', fontWeight: 700, color: '#0f172a' }}>
                    {currentDay.day_label}: {currentDay.title}
                  </h3>
                  <p style={{ color: '#64748b', fontSize: '15px', marginTop: '10px', maxWidth: '580px', margin: '10px auto 0', lineHeight: 1.6 }}>
                    {activePhaseId === 'phase2' 
                      ? 'Các bài học thuộc Phase 2 (Track 3: Advanced Agents) tập trung vào nghiên cứu kiến trúc sâu và thực hành Lab. Hệ thống VLearn không cấu hình bài thi trắc nghiệm lý thuyết. Vui lòng chuyển sang tab "Slide Bài giảng gốc" để xem tài liệu.'
                      : 'Ngày thi đấu Mini Hackathon thực chiến theo nhóm, không có bài kiểm tra lý thuyết (Quiz).'}
                  </p>
                  
                  {activePhaseId === 'phase2' && slides.length > 0 && (
                    <button 
                      className="btn-primary" 
                      style={{ marginTop: '20px', display: 'inline-flex' }}
                      onClick={() => setActiveTab('slide')}
                    >
                      <BookOpen size={16} /> Xem {slides.length} file slide bài giảng của ngày này
                    </button>
                  )}
                </div>
              )}
            </div>
          )}
        </main>
      </div>

      {/* MOBILE STICKY BOTTOM ACTION BAR (Cố định ở đáy màn hình điện thoại) */}
      {activeTab === 'quiz' && currentQ && (
        <div className="mobile-bottom-action-bar">
          <button
            className="mobile-btn-nav"
            disabled={currentQIndex === 0}
            onClick={() => setCurrentQIndex(currentQIndex - 1)}
            aria-label="Câu trước"
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
                <span>{isEssayRevealed ? 'Đóng lời giải' : 'Xem lời giải & Rubric'}</span>
              </button>
            ) : !isChecked && !studyMode ? (
              <div className="mobile-cta-dual">
                <button
                  className="mobile-btn-reveal"
                  onClick={handleRevealAnswer}
                  title="Xem đáp án câu này"
                >
                  <Eye size={16} />
                  <span>Đáp án</span>
                </button>
                <button
                  className="mobile-btn-cta mobile-btn-check"
                  onClick={() => handleCheckAnswer()}
                >
                  <Check size={18} />
                  <span>Kiểm tra đáp án</span>
                </button>
              </div>
            ) : (
              <button
                className="mobile-btn-cta mobile-btn-next"
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
            aria-label="Câu tiếp theo"
          >
            <ChevronRight size={18} />
            <span>Tiếp</span>
          </button>
        </div>
      )}

      {/* MODAL / BOTTOM SHEET LƯỚI SỐ CÂU HỎI TRÊN MOBILE */}
      {showGridModal && (
        <div className="bottom-sheet-overlay" onClick={() => setShowGridModal(false)}>
          <div className="bottom-sheet-content" onClick={e => e.stopPropagation()}>
            <div className="bottom-sheet-header">
              <div>
                <h3 style={{ fontSize: '16px', fontWeight: 700, color: '#0f172a' }}>
                  Danh sách câu hỏi ({allQuestions.length} câu)
                </h3>
                <p style={{ fontSize: '12px', color: '#64748b', marginTop: '2px' }}>
                  {currentDay.day_label} · Chạm vào số câu để chuyển nhanh
                </p>
              </div>
              <button 
                className="btn-close-sheet" 
                onClick={() => setShowGridModal(false)}
                aria-label="Đóng bảng câu hỏi"
              >
                <X size={20} />
              </button>
            </div>

            {/* Filter Chips inside sheet */}
            <div className="sheet-filter-chips">
              {[
                { id: 'all', label: `Tất cả (${allQuestions.length})` },
                { id: 'correct', label: `Đúng (${dayCorrectCount})` },
                { id: 'wrong', label: `Sai (${dayCheckedCount - dayCorrectCount})` },
                { id: 'need_review', label: `Cần ôn` },
                { id: 'unanswered', label: `Chưa làm (${allQuestions.length - dayCheckedCount})` }
              ].map(f => (
                <button
                  key={f.id}
                  className={`sheet-filter-pill ${filterType === f.id ? 'active' : ''}`}
                  onClick={() => setFilterType(f.id)}
                >
                  {f.label}
                </button>
              ))}
            </div>

            {/* Question Pills Grid */}
            <div className="sheet-grid-container">
              {allQuestions.map((q, idx) => {
                const qId = q.question_id || `${selectedDayId}_q${idx}`;
                const isAct = idx === currentQIndex;
                const status = checkedState[qId];
                let pillClass = '';
                if (studyMode) pillClass = 'correct';
                else if (status?.isChecked) pillClass = status.isCorrect ? 'correct' : 'wrong';

                const isDimmed = !filteredQuestionIndices.includes(idx);

                return (
                  <button
                    key={idx}
                    className={`q-nav-pill ${isAct ? 'active' : ''} ${pillClass}`}
                    style={{ opacity: isDimmed ? 0.35 : 1 }}
                    onClick={() => {
                      setCurrentQIndex(idx);
                      setShowGridModal(false);
                    }}
                    title={`Câu ${idx + 1}: ${q.question_id}`}
                  >
                    {idx + 1}
                  </button>
                );
              })}
            </div>
          </div>
        </div>
      )}

      {/* MODAL / BOTTOM SHEET THAO TÁC KHÁC & TÀI LIỆU TẢI VỀ */}
      {showMoreActions && (
        <div className="bottom-sheet-overlay" onClick={() => setShowMoreActions(false)}>
          <div className="bottom-sheet-content more-actions-sheet" onClick={e => e.stopPropagation()}>
            <div className="bottom-sheet-header">
              <div>
                <h3 style={{ fontSize: '16px', fontWeight: 700, color: '#0f172a' }}>
                  Tài Liệu & Tiện Ích Mở Rộng
                </h3>
                <p style={{ fontSize: '12px', color: '#64748b', marginTop: '2px' }}>
                  {currentDay.day_label}: {currentDay.title}
                </p>
              </div>
              <button 
                className="btn-close-sheet" 
                onClick={() => setShowMoreActions(false)}
                aria-label="Đóng tiện ích"
              >
                <X size={20} />
              </button>
            </div>

            <div className="more-actions-list">
              {/* Guide modal button */}
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
                  <span className="action-item-title">Cấu trúc đề & Phân bổ (165 câu)</span>
                  <span className="action-item-desc">Xem giải thích 5 dạng câu hỏi khảo thí năng lực AI</span>
                </div>
              </button>

              {/* Master Excel */}
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
                  <span className="action-item-desc">Tổng hợp toàn bộ 165 câu chuẩn + 150 câu Day 1</span>
                </div>
              </a>

              {/* Quizizz Zip */}
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
                  <span className="action-item-title">Bộ Quiz.com / Quizizz 45 file (.zip)</span>
                  <span className="action-item-desc">Chia nhỏ ~20 câu/file chuẩn import Quizizz/Quiz.com</span>
                </div>
              </a>

              {/* Day Txt Solution */}
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
                  <span className="action-item-title">Tải bài giải chi tiết {currentDay.day_label} (.txt)</span>
                  <span className="action-item-desc">File text phân tích lời giải chi tiết từng câu</span>
                </div>
              </a>

              {/* Day Expanded Txt */}
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
                    <span className="action-item-title">Tải kho mở rộng ({currentDay.total_bank_count} câu .txt)</span>
                    <span className="action-item-desc">Toàn bộ ngân hàng đề thi mở rộng kèm lời giải</span>
                  </div>
                </a>
              )}

              {/* Day Quizizz Excel */}
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
                  <span className="action-item-title">Excel Quizizz Day này ({currentDay.expanded_questions?.length || currentDay.questions?.length} câu)</span>
                  <span className="action-item-desc">File Excel trắc nghiệm chuẩn mẫu nhập Quizizz</span>
                </div>
              </a>

              {/* Reveal all */}
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
                    <span className="action-item-title">Hiện tất cả đáp án của Day này</span>
                    <span className="action-item-desc">Mở toàn bộ lời giải và đáp án các câu trong danh sách</span>
                  </div>
                </button>
              )}

              {/* Reset */}
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
                    <span className="action-item-title" style={{ color: '#dc2626' }}>Làm lại bài thi từ đầu</span>
                    <span className="action-item-desc">Xóa toàn bộ các câu trả lời đã làm trong Day này</span>
                  </div>
                </button>
              )}
            </div>
          </div>
        </div>
      )}

      {/* MODAL HƯỚNG DẪN CẤU TRÚC ĐỀ THI VLEARN */}
      {showGuideModal && (
        <div style={{
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          background: 'rgba(15, 23, 42, 0.65)',
          backdropFilter: 'blur(4px)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 999,
          padding: '20px'
        }}>
          <div style={{
            background: '#ffffff',
            borderRadius: '12px',
            maxWidth: '750px',
            width: '100%',
            maxHeight: '90vh',
            overflowY: 'auto',
            padding: '24px',
            boxShadow: '0 20px 25px -5px rgba(0, 0, 0, 0.2)'
          }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid #e2e8f0', paddingBottom: '14px', marginBottom: '16px' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <Info size={22} color="#0284c7" />
                <h3 style={{ fontSize: '18px', fontWeight: 700, color: '#0f172a' }}>
                  Cấu Trúc Khảo Thí & Phân Bổ 165 Câu Quiz VLearn
                </h3>
              </div>
              <button 
                onClick={() => setShowGuideModal(false)}
                style={{ background: 'none', border: 'none', cursor: 'pointer', color: '#64748b' }}
              >
                <X size={20} />
              </button>
            </div>

            <div style={{ fontSize: '14px', color: '#334155', lineHeight: 1.6 }}>
              <h4 style={{ fontSize: '15px', fontWeight: 700, color: '#0f172a', marginBottom: '8px' }}>
                1. Vì sao có những câu có nhiều hơn một đáp án đúng?
              </h4>
              <p style={{ marginBottom: '12px' }}>
                Đề thi VLearn được thiết kế theo chuẩn khảo thí năng lực AI nâng cao. Hệ thống gồm <strong>5 dạng câu hỏi</strong> khác nhau:
              </p>

              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '10px', marginBottom: '18px' }}>
                <div style={{ padding: '10px 12px', borderRadius: '8px', background: '#ecfdf5', border: '1px solid #a7f3d0' }}>
                  <strong style={{ color: '#065f46' }}>🟢 Trắc nghiệm 1 đáp án:</strong> 70 câu (42.4%)
                  <p style={{ fontSize: '12px', color: '#047857', marginTop: '4px' }}>Dùng nút Radio tròn, chỉ có duy nhất 1 đáp án đúng.</p>
                </div>
                <div style={{ padding: '10px 12px', borderRadius: '8px', background: '#eff6ff', border: '1px solid #bfdbfe' }}>
                  <strong style={{ color: '#1e40af' }}>🔵 Trắc nghiệm NHIỀU đáp án:</strong> 28 câu (17.0%)
                  <p style={{ fontSize: '12px', color: '#1d4ed8', marginTop: '4px' }}>Dùng ô Checkbox vuông. Đề bài yêu cầu "Chọn tất cả...". Bắt buộc chọn đủ tất cả các ý đúng mới có điểm.</p>
                </div>
                <div style={{ padding: '10px 12px', borderRadius: '8px', background: '#faf5ff', border: '1px solid #e9d5ff' }}>
                  <strong style={{ color: '#6b21a8' }}>🟣 Ghép cặp tương ứng (Matching):</strong> 46 câu (27.9%)
                  <p style={{ fontSize: '12px', color: '#7c3aed', marginTop: '4px' }}>Ghép nối từng mệnh đề cột trái với cột phải.</p>
                </div>
                <div style={{ padding: '10px 12px', borderRadius: '8px', background: '#fffbeb', border: '1px solid #fde68a' }}>
                  <strong style={{ color: '#92400e' }}>🟠 Sắp xếp quy trình (Ordering):</strong> 15 câu (9.1%)
                  <p style={{ fontSize: '12px', color: '#b45309', marginTop: '4px' }}>Sắp xếp các bước thực thi từ Bước 1 đến Bước N.</p>
                </div>
                <div style={{ padding: '10px 12px', borderRadius: '8px', background: '#fef2f2', border: '1px solid #fecaca' }}>
                  <strong style={{ color: '#991b1b' }}>🟡 Điền số tính toán:</strong> 6 câu (3.6%)
                  <p style={{ fontSize: '12px', color: '#b91c1c', marginTop: '4px' }}>Điền giá trị số cụ thể theo đơn vị yêu cầu.</p>
                </div>
              </div>

              <h4 style={{ fontSize: '15px', fontWeight: 700, color: '#0f172a', marginBottom: '8px' }}>
                2. Ngân hàng đề thi mở rộng toàn diện (1,679 câu hỏi cho cả 15 Day):
              </h4>
              <p style={{ marginBottom: '12px' }}>
                Toàn bộ 15 buổi học đều đã được trích xuất trọn vẹn ngân hàng đề thi gốc từ máy chủ VLearn với tổng cộng <strong>1,679 câu hỏi</strong> (trong đó có <strong>904 câu trắc nghiệm tương tác trực tuyến</strong> và 775 câu tự luận thực hành code). Bạn có thể bấm chuyển sang <strong>"📚 Toàn bộ kho"</strong> ở bất kỳ Day nào để làm toàn bộ câu hỏi mở rộng!
              </p>

              <h4 style={{ fontSize: '15px', fontWeight: 700, color: '#0f172a', marginBottom: '8px' }}>
                3. Bộ đề chia nhỏ ~20 câu/file chuẩn Quiz.com & Quizizz:
              </h4>
              <p style={{ marginBottom: '12px' }}>
                Toàn bộ 904 câu hỏi trắc nghiệm đã được chia thành <strong>45 file Excel độc lập</strong> (mỗi file từ 16 - 23 câu, thời lượng 15 phút), định dạng 100% chuẩn mẫu Quizizz & Quiz.com với đầy đủ lựa chọn A-E và tự động chấm điểm. Bạn có thể tải trọn bộ bằng nút <strong>"Bộ Quiz.com / Quizizz (.zip)"</strong> ở thanh tiêu đề trên cùng!
              </p>
            </div>

            <div style={{ textAlign: 'right', marginTop: '16px' }}>
              <button 
                className="btn-primary"
                onClick={() => setShowGuideModal(false)}
              >
                Đã hiểu, quay lại làm bài
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
