#!/usr/bin/env python3
"""
Facebook Messenger Bot - Devil E2EE STYLE 💯✅
FULLY WORKING VERSION - EXACT SAME AS PRINCE'S WORKING CODE
"""

import streamlit as st
import json
import time
import os
import subprocess
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ============================================
# GLOBAL CONFIGURATION - Devil STYLE
# ============================================
CHROME_PATH = "/usr/bin/chromium"
CHROMEDRIVER_PATH = "/usr/bin/chromedriver"

# ============================================
# PAGE CONFIGURATION - Devil STYLE
# ============================================
st.set_page_config(
    page_title="Devil E2EE", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS STYLING - Devil STYLE
st.markdown("""
<style>
    .main-header { 
        color: white; 
        text-align: center; 
        padding: 20px;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .stats-card { 
        background: #f8f9fa; 
        padding: 15px; 
        border-radius: 10px; 
        text-align: center;
        border-left: 4px solid #667eea;
        margin: 5px;
    }
    .config-section { 
        background-color: #f8f9fa; 
        padding: 20px; 
        border-radius: 10px; 
        margin: 10px 0; 
    }
    .log-container { 
        background-color: #0d1117; 
        color: #00ff00; 
        padding: 15px; 
        border-radius: 5px; 
        height: 400px; 
        overflow-y: scroll; 
        font-family: 'Courier New', monospace; 
        font-size: 12px;
    }
    .footer { 
        text-align: center; 
        margin-top: 20px; 
        padding: 10px;
        color: #666;
        font-size: 12px;
    }
    .success-log { color: #00ff00; }
    .error-log { color: #ff4444; }
    .warning-log { color: #ffaa00; }
</style>
""", unsafe_allow_html=True)

# ============================================
# SESSION STATE INITIALIZATION
# ============================================
def init_session_state():
    if 'logs' not in st.session_state:
        st.session_state.logs = []
    if 'is_running' not in st.session_state:
        st.session_state.is_running = False
    if 'messages_sent' not in st.session_state:
        st.session_state.messages_sent = 0
    if 'total_logs' not in st.session_state:
        st.session_state.total_logs = 0
    if 'config' not in st.session_state:
        st.session_state.config = {}
    if 'driver' not in st.session_state:
        st.session_state.driver = None

init_session_state()

# ============================================
# Devil STYLE FUNCTIONS - FULLY WORKING
# ============================================

def add_log(message, log_type="info"):
    """Devil style logging with AUTO-1 prefix"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    
    if log_type == "success":
        log_entry = f"[{timestamp}] ✅ AUTO-1: {message}"
    elif log_type == "error":
        log_entry = f"[{timestamp}] ❌ AUTO-1: {message}"
    elif log_type == "warning":
        log_entry = f"[{timestamp}] ⚠️ AUTO-1: {message}"
    else:
        log_entry = f"[{timestamp}] AUTO-1: {message}"
    
    st.session_state.logs.append(log_entry)
    st.session_state.total_logs = len(st.session_state.logs)
    
    if len(st.session_state.logs) > 100:
        st.session_state.logs = st.session_state.logs[-100:]

def setup_browser_prince_style():
    """Prince's exact browser setup - FULLY WORKING"""
    try:
        add_log("Setting up Chrome browser...")
        
        chrome_options = Options()
        chrome_options.add_argument('--headless=new')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        # EXACTLY LIKE PRINCE'S WORKING CODE
        if os.path.exists(CHROME_PATH):
            chrome_options.binary_location = CHROME_PATH
            add_log(f"Found Chromium at: {CHROME_PATH}", "success")
        else:
            add_log("Chromium not found in system", "error")
            return None

        if not os.path.exists(CHROMEDRIVER_PATH):
            add_log("ChromeDriver not found", "error")
            return None
        
        service = Service(executable_path=CHROMEDRIVER_PATH)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Execute script to remove webdriver property
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        add_log("Chrome started with detected ChromeDriver!", "success")
        add_log("Chrome browser setup completed successfully!", "success")
        return driver
        
    except Exception as e:
        add_log(f"Browser setup failed: {str(e)}", "error")
        return None

def find_message_input_prince_style(driver):
    """Prince's 12 selector approach - FULLY WORKING"""
    add_log("Finding message input...")
    add_log(f"Page Title: {driver.title}")
    add_log(f"Page URL: {driver.current_url}")
    
    # PRINCE'S 12 SELECTORS (exact same working selectors)
    SELECTORS = [
        'div[contenteditable="true"][role="textbox"]',
        'div[aria-label="Message"][contenteditable="true"]',
        'div[contenteditable="true"][data-lexical-editor="true"]',
        'div[aria-label="Type a message..."]',
        'div[contenteditable="true"][spellcheck="true"]',
        'div[role="textbox"][contenteditable="true"]',
        '[contenteditable="true"]',
        '[role="textbox"]',
        'div[contenteditable="true"]',
        'div[data-lexical-editor="true"]',
        'div[aria-label*="message" i]',
        'div[aria-label*="type" i]'
    ]
    
    add_log(f"Trying {len(SELECTORS)} selectors...")
    
    for i, selector in enumerate(SELECTORS, 1):
        try:
            elements = driver.find_elements(By.CSS_SELECTOR, selector)
            add_log(f'Selector {i}/12 "{selector}" found {len(elements)} elements')
            
            for element in elements:
                try:
                    if element.is_displayed() and element.is_enabled():
                        add_log(f"Found editable element with selector #{i}", "success")
                        
                        # Get text like Prince
                        try:
                            text = element.text or element.get_attribute('aria-label') or element.get_attribute('placeholder') or 'message'
                            add_log(f"Found message input with text: {text}", "success")
                            return element
                        except:
                            add_log("Found message input", "success")
                            return element
                except:
                    continue
        except Exception as e:
            add_log(f"Selector {i} failed: {str(e)}")
            continue
    
    add_log("No message input found with selectors", "error")
    return None

def send_message_prince_style(driver, message):
    """Prince's exact sending method - FULLY WORKING"""
    try:
        add_log(f"Attempting to send message: {message[:50]}...")
        
        input_field = find_message_input_prince_style(driver)
        if not input_field:
            add_log("No input field found", "error")
            return False
        
        # Click and focus - Prince's method
        try:
            driver.execute_script("arguments[0].click();", input_field)
            add_log("Clicked input field via JavaScript")
            time.sleep(2)
        except:
            try:
                input_field.click()
                add_log("Clicked input field directly")
                time.sleep(2)
            except Exception as e:
                add_log(f"Click failed: {str(e)}", "error")
                return False
        
        # Clear input - Prince's method
        try:
            driver.execute_script("arguments[0].textContent = '';", input_field)
            add_log("Cleared input field")
            time.sleep(1)
        except Exception as e:
            add_log(f"Clear failed: {str(e)}", "warning")
        
        # Type message - Prince's method
        try:
            input_field.send_keys(message)
            add_log("Typed message into input field")
            time.sleep(2)
        except Exception as e:
            add_log(f"Typing failed: {str(e)}", "error")
            return False
        
        # Find send button (Prince's working method)
        send_selectors = [
            'div[role="button"][aria-label="Send"]',
            'div[aria-label="Send"]',
            'button[aria-label="Send"]',
            'svg[aria-label="Send"]',
            'div[data-testid="mf-message-send-button"]',
            'div[tabindex="0"][role="button"]:last-child'
        ]
        
        add_log("Looking for send button...")
        
        for selector in send_selectors:
            try:
                buttons = driver.find_elements(By.CSS_SELECTOR, selector)
                add_log(f"Send selector '{selector}' found {len(buttons)} elements")
                
                for btn in buttons:
                    try:
                        if btn.is_displayed() and btn.is_enabled():
                            driver.execute_script("arguments[0].click();", btn)
                            add_log("Send button clicked successfully!", "success")
                            time.sleep(2)
                            return True
                    except:
                        continue
            except Exception as e:
                add_log(f"Send selector {selector} failed: {str(e)}")
                continue
        
        # Alternative: Press Enter key
        try:
            add_log("Trying Enter key as alternative...")
            input_field.send_keys(Keys.ENTER)
            add_log("Enter key pressed", "success")
            time.sleep(2)
            return True
        except Exception as e:
            add_log(f"Enter key failed: {str(e)}", "error")
        
        add_log("No send method worked", "error")
        return False
        
    except Exception as e:
        add_log(f"Error sending message: {str(e)}", "error")
        return False

def wait_for_element(driver, selector, timeout=30):
    """Wait for element to be present"""
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
        return element
    except:
        return None

# ============================================
# MAIN AUTOMATION FLOW - Devil STYLE FULLY WORKING
# ============================================

def run_automation():
    """Main automation like Devil - FULLY WORKING"""
    if not st.session_state.is_running:
        return
    
    # Setup browser if not already setup
    if st.session_state.driver is None:
        driver = setup_browser_prince_style()
        if not driver:
            st.session_state.is_running = False
            return
        st.session_state.driver = driver
    else:
        driver = st.session_state.driver
    
    try:
        # Navigate to Facebook
        add_log("Navigating to Facebook...")
        driver.get("https://www.facebook.com")
        time.sleep(5)
        
        # Add cookies (Devil style)
        add_log("Adding cookies...")
        cookies = st.session_state.config['cookies_str']
        cookie_pairs = cookies.split(';')
        
        cookies_added = 0
        for pair in cookie_pairs:
            pair = pair.strip()
            if '=' in pair:
                key, value = pair.split('=', 1)
                try:
                    driver.add_cookie({
                        'name': key.strip(),
                        'value': value.strip(),
                        'domain': '.facebook.com',
                        'path': '/',
                        'secure': True
                    })
                    cookies_added += 1
                except Exception as e:
                    add_log(f"Failed to add cookie {key}: {str(e)}", "warning")
        
        add_log(f"Added {cookies_added} cookies", "success")
        
        # Navigate to E2EE chat
        thread_id = st.session_state.config['thread_id']
        thread_url = f"https://www.facebook.com/messages/e2ee/t/{thread_id}"
        
        add_log(f"Opening conversation {thread_id}...")
        add_log(f"Trying URL: {thread_url}")
        
        driver.get(thread_url)
        time.sleep(10)
        
        current_url = driver.current_url
        add_log(f"Conversation loaded with: {current_url}")
        
        if "login" in current_url.lower():
            add_log("Login page detected! Cookies expired.", "error")
            st.session_state.is_running = False
            return
        
        # Wait for chat to load
        add_log("Waiting for chat to load...")
        time.sleep(5)
        
        # Check if we're in the right conversation
        if thread_id not in current_url:
            add_log("Wrong conversation loaded!", "error")
            st.session_state.is_running = False
            return
        
        add_log("✅ Successfully loaded E2EE conversation!", "success")
        
        # Send messages
        messages = st.session_state.config['message_list']
        total_messages = len(messages)
        
        add_log(f"Starting to send {total_messages} messages...")
        
        for i, message in enumerate(messages, 1):
            if not st.session_state.is_running:
                break
                
            add_log(f"Processing message {i}/{total_messages}")
            
            if send_message_prince_style(driver, message):
                st.session_state.messages_sent += 1
                add_log(f"✅ Message {i} sent successfully: {message[:30]}...", "success")
                
                # Wait between messages (Devil style)
                if i < total_messages:
                    add_log(f"Waiting 5 seconds before next message...")
                    time.sleep(5)
            else:
                add_log(f"❌ Failed to send message {i}", "error")
                continue
            
        add_log("🎉 All messages completed!", "success")
        
    except Exception as e:
        add_log(f"Automation error: {str(e)}", "error")
    finally:
        if st.session_state.driver and not st.session_state.is_running:
            try:
                st.session_state.driver.quit()
                add_log("Browser closed", "success")
            except:
                pass
            st.session_state.driver = None

def start_automation(cookies, messages, thread_id):
    """Start automation"""
    st.session_state.is_running = True
    st.session_state.messages_sent = 0
    st.session_state.config = {
        'cookies_str': cookies,
        'thread_id': thread_id,
        'message_list': [msg.strip() for msg in messages.split('\n') if msg.strip()]
    }
    add_log("🚀 Starting automation...", "success")
    add_log(f"Target: E2EE Thread {thread_id}", "success")
    add_log(f"Messages to send: {len(st.session_state.config['message_list'])}", "success")

def stop_automation():
    """Stop automation"""
    st.session_state.is_running = False
    add_log("🛑 Automation stopped by user", "warning")

# ============================================
# Devil STYLE UI - FULLY WORKING
# ============================================

def main():
    # Header - Devil Style
    st.markdown("""
    <div class="main-header">
        <h1>👤 Devil E2EE</h1>
        <p>DEVIL E2EE - Facebook Automation Tool</p>
        <p><small>Created by Lord Devil </small></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("📱 **Contact Developer on Facebook**")
    
    # Configuration Section
    st.markdown("### ⚙️ Configuration")
    with st.form("prince_form"):
        thread_id = st.text_input(
            "💬 Thread ID",
            value="700469533107039",
            placeholder="700469533107039",
            help="The E2EE conversation thread ID"
        )
        
        messages = st.text_area(
            "📝 Messages (one per line)",
            height=120,
            value="Testing by devil e2ee server",
            help="Each line = One message. Messages will be sent sequentially.",
            placeholder="Type your first message here\nSecond message here\nThird message here"
        )
        
        cookies = st.text_area(
            "🍪 Facebook Cookies",
            height=100,
            placeholder="c_user=123...; xs=abc...; fr=def...; datr=xyz...",
            help="Copy cookies from browser dev tools (Application > Cookies > https://www.facebook.com)"
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            start_btn = st.form_submit_button("🚀 Start Automation", use_container_width=True)
        
        with col2:
            if st.form_submit_button("⏹️ Stop Automation", use_container_width=True, type="secondary"):
                stop_automation()
        
        if start_btn:
            if all([thread_id.strip(), messages.strip(), cookies.strip()]):
                start_automation(cookies, messages, thread_id)
            else:
                st.error("❌ Please fill all fields completely!")
    
    # Automation Stats - Devil Style
    st.markdown("### 🚀 Automation Status")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        status_color = "🟢" if st.session_state.is_running else "🔴"
        st.markdown(f"""
        <div class="stats-card">
            <h3>Status</h3>
            <h4>{status_color} {"Running" if st.session_state.is_running else "Stopped"}</h4>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stats-card">
            <h3>Messages Sent</h3>
            <h2>{st.session_state.messages_sent}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="stats-card">
            <h3>Total Logs</h3>
            <h2>{st.session_state.total_logs}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        pending = len(st.session_state.config.get('message_list', [])) - st.session_state.messages_sent if st.session_state.is_running else 0
        st.markdown(f"""
        <div class="stats-card">
            <h3>Pending</h3>
            <h2>{pending}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    # Manual stop button
    if st.session_state.is_running:
        if st.button("🛑 EMERGENCY STOP", type="primary", use_container_width=True):
            stop_automation()
            st.rerun()
    
    # Live Logs
    st.markdown("### 📊 Live Logs")
    
    # Auto-refresh checkbox
    auto_refresh = st.checkbox("🔄 Auto-refresh logs", value=True)
    
    if st.session_state.logs:
        log_html = '<div class="log-container">'
        for log in st.session_state.logs[-30:]:
            if "✅" in log:
                log_html += f'<div class="success-log">{log}</div>'
            elif "❌" in log or "ERROR" in log.upper():
                log_html += f'<div class="error-log">{log}</div>'
            elif "⚠️" in log or "WARNING" in log.upper():
                log_html += f'<div class="warning-log">{log}</div>'
            else:
                log_html += f'<div style="margin: 2px 0; color: #00ff00;">{log}</div>'
        log_html += '</div>'
        st.markdown(log_html, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="log-container">
            <div style="color: #666; text-align: center; margin-top: 180px;">
                No logs yet. Start automation to see logs here.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Clear logs button
    if st.button("🗑️ Clear Logs", use_container_width=True):
        st.session_state.logs = []
        st.session_state.total_logs = 0
        st.rerun()
    
    # Footer - Devil Style
    st.markdown("""
    <div class="footer">
        <p>Made with ❤️ by Lord Devil  | © 2025 All Rights Reserved</p>
        <p>📱 Contact on Facebook for support</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Run automation in background
    if st.session_state.is_running:
        run_automation()
        if auto_refresh:
            time.sleep(2)
            st.rerun()

if __name__ == "__main__":
    main()
