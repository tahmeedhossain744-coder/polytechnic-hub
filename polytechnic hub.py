<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CST Campus Hub - Pabna Polytechnic Institute</title>
    <style>
        :root {
            --bg-color: #0d1117;
            --card-bg: #161b22;
            --accent-gold: #d4af37;
            --text-color: #f0f6fc;
            --text-secondary: #8b949e;
            --border-color: #30363d;
            --info-bg: rgba(56, 139, 253, 0.1);
            --info-border: rgba(56, 139, 253, 0.4);
            --success-bg: rgba(46, 160, 67, 0.15);
            --success-border: rgba(46, 160, 67, 0.4);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.6;
            padding: 20px;
        }

        .container {
            max-width: 850px;
            margin: 0 auto;
        }

        h1, h2, h3, h4 {
            color: var(--accent-gold);
        }

        hr {
            border: 0;
            height: 1px;
            background: var(--border-color);
            margin: 20px 0;
        }

        a {
            color: #58a6ff;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        /* Header */
        header h2 {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        /* Hero Section */
        .hero {
            text-align: center;
            padding: 30px;
            background: linear-gradient(180deg, rgba(212, 175, 55, 0.1) 0%, rgba(13, 17, 23, 0) 100%);
            border-radius: 12px;
            border: 1px solid var(--border-color);
            margin-bottom: 25px;
        }

        .hero h1 {
            margin-bottom: 10px;
            font-size: 1.8rem;
        }

        /* Grid Layout */
        .grid-2 {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }

        @media (max-width: 768px) {
            .grid-2 {
                grid-template-columns: 1fr;
            }
        }

        /* Info & Alert Boxes */
        .info-box {
            background-color: var(--info-bg);
            border: 1px solid var(--info-border);
            border-radius: 8px;
            padding: 15px;
            margin-top: 10px;
            margin-bottom: 20px;
            font-size: 0.95rem;
        }

        .info-box ul {
            padding-left: 20px;
        }

        .info-box li {
            margin-bottom: 12px;
        }

        .success-box {
            background-color: var(--success-bg);
            border: 1px solid var(--success-border);
            color: #3fb950;
            border-radius: 8px;
            padding: 12px 15px;
            margin-top: 15px;
            font-weight: 500;
        }

        /* Button */
        .btn {
            background-color: var(--card-bg);
            color: var(--text-color);
            border: 1px solid var(--border-color);
            padding: 10px 16px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 0.95rem;
            margin-top: 10px;
            transition: all 0.2s ease;
        }

        .btn:hover {
            border-color: var(--accent-gold);
            color: var(--accent-gold);
        }

        #notification-area {
            display: none;
        }

        /* Routine List */
        .routine-list {
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 15px 25px;
            margin-top: 10px;
            max-height: 450px;
            overflow-y: auto;
        }

        .routine-list li {
            margin-bottom: 6px;
            font-size: 0.95rem;
        }

        /* AI Chat Section */
        .chat-container {
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 15px;
            margin-top: 10px;
        }

        .chat-messages {
            max-height: 300px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin-bottom: 15px;
        }

        .message {
            padding: 10px 14px;
            border-radius: 8px;
            max-width: 85%;
            font-size: 0.95rem;
        }

        .message.assistant {
            background-color: #21262d;
            border: 1px solid var(--border-color);
            align-self: flex-start;
        }

        .message.user {
            background-color: rgba(212, 175, 55, 0.15);
            border: 1px solid var(--accent-gold);
            align-self: flex-end;
        }

        .chat-input-form {
            display: flex;
            gap: 10px;
        }

        .chat-input-form input {
            flex: 1;
            background-color: var(--bg-color);
            border: 1px solid var(--border-color);
            color: var(--text-color);
            padding: 10px 14px;
            border-radius: 6px;
            font-size: 0.95rem;
            outline: none;
        }

        .chat-input-form input:focus {
            border-color: var(--accent-gold);
        }

        /* Team Section */
        .team-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
            margin-top: 15px;
        }

        @media (max-width: 768px) {
            .team-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        .team-card {
            background-color: var(--card-bg);
            padding: 15px;
            border-radius: 8px;
            border: 1px solid var(--border-color);
            text-align: center;
        }

        .team-card h4 {
            color: var(--text-color);
            margin-bottom: 5px;
        }

        .team-card p {
            color: var(--accent-gold);
            font-weight: bold;
            font-size: 13px;
        }
    </style>
</head>
<body>

<div class="container">
    <!-- Header Section -->
    <header>
        <h2><span>💻 CST Campus Hub</span></h2>
    </header>
    <hr>

    <!-- Hero Section -->
    <div class="hero">
        <h1>পাবনা সরকারি পলিটেকনিক ইনস্টিটিউট</h1>
        <p>কম্পিউটার সায়েন্স অ্যান্ড টেকনোলজি (1st--CST) — গ্রুপ B</p>
    </div>

    <!-- Main Grid Layout -->
    <div class="grid-2">
        <!-- Column 1: Notice Board & Quick Action -->
        <div>
            <h3>📌 নোটিশ বোর্ড</h3>
            <div class="info-box">
                <ul>
                    <li>১ম সেমিস্টার ক্লাস টেস্টের সময়সূচী প্রকাশিত হয়েছে।</li>
                    <li>ল্যাব প্র্যাকটিক্যাল অ্যাসাইনমেন্ট জমা দিন।</li>
                    <li>CST গ্রুপের নতুন ওয়েবসাইট লঞ্চ করা হয়েছে।</li>
                    <li>নতুন প্রজেক্ট টিমের সাথে পরিচিত হোন।</li>
                    <li>আগামী সপ্তাহে সেমিস্টার ফাইনাল পরীক্ষা অনুষ্ঠিত হবে। আগামী ০৭ তারিখ রোজ বৃহস্পতিবার থেকে ১২ তারিখ রোজ রবিবার পর্যন্ত কলেজ বন্ধ থাকবে। তাই সকল শিক্ষার্থীকে অনুরোধ করা হচ্ছে যে, এই সময়ের মধ্যে সকল অ্যাসাইনমেন্ট এবং প্রজেক্ট তৈরি করবেন। আর ১৩ তারিখ রোজ সোমবার থেকে ক্লাস শুরু হবে। সকল শিক্ষার্থীকে অনুরোধ করা হচ্ছে যে সকলেই সবার অ্যাসাইনমেন্ট এবং প্রজেক্ট জমা দিবেন।</li>
                    <li>সকল্কে সবাই নিজেদের উপবিত্তির জন্য প্রদান ক্রিত বিকাশ, নগদ, রকেট এবং ব্যাংক একাউন্টের স্টেটমেন্ট জমা দেওয়ার জন্য অনুরোধ করা হল।</li>
                </ul>
            </div>

            <h3>🔗 কুইক অ্যাকশন সবাইকেই অংশগ্রহন করতে হবে</h3>
            <button class="btn" onclick="activateNotification()">নোটিফিকেশন অন করুন</button>

            <div id="notification-area">
                <div class="success-box">সফল! আপডেট লাইভ দেওয়া হয়েছে!</div>
                <div class="info-box">
                    <p>আপনি এখন থেকে নতুন নোটিশ এবং রুটিন আপডেট পাবেন।</p>
                    <br>
                    <p>আপডেটের জন্য ধন্যবাদ! আপনার CST AI সহকারী।</p>
                </div>
                <p style="margin-bottom: 8px;">আমদের সাথে যোগাযোগ করুন: <a href="https://www.cstprotel.com" target="_blank">CST AI সহকারী</a></p>
                <p>আমাদের টিমের সাথে যোগাযোগ করুন: 
                    <a href="whatsapp://send?phone=01341725738">tahmeed (WhatsApp)</a> / 
                    <a href="https://www.linkedin.com/in/tahmeed/" target="_blank">tahmeed (LinkedIn)</a> / 
                    <a href="https://www.linkedin.com/in/nirab-rahman-2b0a1b1b3/" target="_blank">nirab</a>
                </p>
            </div>
        </div>

        <!-- Column 2: Routine -->
        <div>
            <h3>📅 ক্লাস রুটিন</h3>
            <ul class="routine-list">
                <li>১০:০০ AM - Computer Application</li>
                <li>১১:০০ AM - Basic Electronics</li>
                <li>১২:০০ PM - Mathematics-1</li>
                <li>১২:৩০ PM - Mathematics-2</li>
                <li>০১:০০ PM - Lunch Break</li>
                <li>০২:০০ PM - Physics-1</li>
                <li>০২:৩০ PM - Physics-2</li>
                <li>০৩:০০ PM - Chemistry-1</li>
                <li>০৩:৩০ PM - Chemistry-2</li>
                <li>০৪:০০ PM - English-1</li>
                <li>০৪:৩০ PM - English-2</li>
                <li>০৫:০০ PM - Engineering Drawing</li>
                <li>০৫:০০ PM - Programming Fundamentals</li>
                <li>০৬:০০ PM - Lab Session</li>
                <li>০৭:০০ PM - End of Day</li>
                <li>০৮:০০ PM - Optional Study Time</li>
                <li>০৯:০০ PM - Group Discussion</li>
                <li>১০:০০ PM - Wrap Up and Review</li>
                <li>১১:০০ PM - End of Routine</li>
                <li>১২:০০ AM - Night Study (Optional)</li>
                <li>০১:০০ AM - Sleep Time</li>
                <li>০২:০০ AM - Midnight Snack (Optional)</li>
                <li>০৩:০০ AM - Late Night Study (Optional)</li>
                <li>০৪:০০ AM - Early Morning Exercise (Optional)</li>
                <li>০৫:০০ AM - Breakfast</li>
            </ul>
        </div>
    </div>

    <!-- AI Chat Section -->
    <hr>
    <h3>🤖 CST AI সহকারী</h3>
    <div class="chat-container">
        <div class="chat-messages" id="chat-messages">
            <div class="message assistant">
                হ্যালো! আমি আপনার CST AI সহকারী। রুটিন বা নোটিশ সম্পর্কে কিছু জানতে চান?
            </div>
        </div>
        <form class="chat-input-form" onsubmit="handleChat(event)">
            <input type="text" id="user-input" placeholder="কিছু জিজ্ঞেস করুন..." required autocomplete="off">
            <button type="submit" class="btn" style="margin-top: 0;">পাঠান</button>
        </form>
    </div>

    <!-- Team Section -->
    <hr>
    <h3 style="text-align: center;">🚀 প্রজেক্ট টিম</h3>
    <div class="team-grid">
        <div class="team-card">
            <h4>তাহমিদ</h4>
            <p>Software Engineer</p>
        </div>
        <div class="team-card">
            <h4>নিরব</h4>
            <p>Project Manager</p>
        </div>
        <div class="team-card">
            <h4>mehedi</h4>
            <p>UI/UX Designer</p>
        </div>
        <div class="team-card">
            <h4>prithibi</h4>
            <p>Backend Developer</p>
        </div>
    </div>
</div>

<script>
    // Notification Button Logic
    function activateNotification() {
        const notifArea = document.getElementById('notification-area');
        notifArea.style.display = 'block';
    }

    // AI Chat Logic
    function handleChat(event) {
        event.preventDefault();
        const inputField = document.getElementById('user-input');
        const chatMessages = document.getElementById('chat-messages');
        const userText = inputField.value.trim();

        if (!userText) return;

        // Add User Message
        const userDiv = document.createElement('div');
        userDiv.className = 'message user';
        userDiv.textContent = userText;
        chatMessages.appendChild(userDiv);

        // Generate AI Reply
        const textLower = userText.toLowerCase();
        let aiReply = "";

        if (textLower.includes("routine") || textLower.includes("রুটিন")) {
            aiReply = "আজকের রুটিনে ১০টায় Computer Application এবং ১১টায় Basic Electronics ক্লাস রয়েছে!";
        } else if (textLower.includes("notice") || textLower.includes("নোটিশ")) {
            aiReply = "নতুন নোটিশ অনুযায়ী আগামী সপ্তাহে সেমিস্টার ফাইনাল পরীক্ষা অনুষ্ঠিত হবে এবং আগামী ৭ থেকে ১২ তারিখ পর্যন্ত কলেজ বন্ধ থাকবে।";
        } else if (textLower.includes("team") || textLower.includes("টিম")) {
            aiReply = "এই প্রজেক্টের টিম মেম্বাররা হলেন: তাহমিদ (Software Engineer), নিরব (Project Manager), mehedi (UI/UX Designer), এবং prithibi (Backend Developer)।";
        } else {
            aiReply = "দুঃখিত, আমি এই মুহূর্তে অফলাইনে আছি। তবে টিম খুব শীঘ্রই আমাকে ফুল-স্ট্যাক AI হিসেবে আপডেট করবে!";
        }

        // Add Assistant Message
        setTimeout(() => {
            const aiDiv = document.createElement('div');
            aiDiv.className = 'message assistant';
            aiDiv.textContent = aiReply;
            chatMessages.appendChild(aiDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }, 300);

        // Clear input and scroll
        inputField.value = '';
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
</script>

</body>
</html>
