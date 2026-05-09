"""
登录接口测试用例

使用 pytest 和 requests 库进行登录接口测试
"""

import pytest
import requests
from typing import Dict, Any


# 配置基础信息
BASE_URL = "http://localhost:8000"  # 根据实际情况修改
LOGIN_ENDPOINT = "/api/login"


class TestLoginAPI:
    """登录接口测试类"""

    @pytest.fixture
    def base_url(self):
        """返回基础 URL"""
        return BASE_URL

    @pytest.fixture
    def login_url(self, base_url):
        """返回登录接口完整 URL"""
        return f"{base_url}{LOGIN_ENDPOINT}"

    def test_login_success(self, login_url):
        """测试登录成功场景"""
        payload = {
            "username": "testuser",
            "password": "correct_password"
        }
        
        response = requests.post(login_url, json=payload)
        
        assert response.status_code == 200
        data = response.json()
        assert data.get("success") is True
        assert "token" in data or "access_token" in data
        print(f"✓ 登录成功，获取到 token")

    def test_login_wrong_password(self, login_url):
        """测试密码错误场景"""
        payload = {
            "username": "testuser",
            "password": "wrong_password"
        }
        
        response = requests.post(login_url, json=payload)
        
        assert response.status_code in [401, 403]
        data = response.json()
        assert data.get("success") is False
        print(f"✓ 密码错误，返回预期错误")

    def test_login_user_not_found(self, login_url):
        """测试用户不存在场景"""
        payload = {
            "username": "nonexistent_user",
            "password": "any_password"
        }
        
        response = requests.post(login_url, json=payload)
        
        assert response.status_code in [401, 403, 404]
        data = response.json()
        assert data.get("success") is False
        print(f"✓ 用户不存在，返回预期错误")

    def test_login_empty_username(self, login_url):
        """测试用户名为空场景"""
        payload = {
            "username": "",
            "password": "some_password"
        }
        
        response = requests.post(login_url, json=payload)
        
        assert response.status_code in [400, 422]
        print(f"✓ 用户名为空，返回验证错误")

    def test_login_empty_password(self, login_url):
        """测试密码为空场景"""
        payload = {
            "username": "testuser",
            "password": ""
        }
        
        response = requests.post(login_url, json=payload)
        
        assert response.status_code in [400, 422]
        print(f"✓ 密码为空，返回验证错误")

    def test_login_missing_username(self, login_url):
        """测试缺少用户名字段场景"""
        payload = {
            "password": "some_password"
        }
        
        response = requests.post(login_url, json=payload)
        
        assert response.status_code in [400, 422]
        print(f"✓ 缺少用户名，返回验证错误")

    def test_login_missing_password(self, login_url):
        """测试缺少密码字段场景"""
        payload = {
            "username": "testuser"
        }
        
        response = requests.post(login_url, json=payload)
        
        assert response.status_code in [400, 422]
        print(f"✓ 缺少密码，返回验证错误")

    def test_login_invalid_json(self, login_url):
        """测试发送无效 JSON 场景"""
        headers = {"Content-Type": "application/json"}
        
        response = requests.post(
            login_url, 
            data="invalid json{", 
            headers=headers
        )
        
        assert response.status_code in [400, 422]
        print(f"✓ 无效 JSON，返回解析错误")

    def test_login_get_method_not_allowed(self, login_url):
        """测试使用 GET 方法访问登录接口（应该不允许）"""
        payload = {
            "username": "testuser",
            "password": "some_password"
        }
        
        response = requests.get(login_url, params=payload)
        
        assert response.status_code in [405, 404, 400]
        print(f"✓ GET 方法不被允许")

    def test_login_sql_injection_attempt(self, login_url):
        """测试 SQL 注入尝试场景"""
        payload = {
            "username": "' OR '1'='1",
            "password": "' OR '1'='1"
        }
        
        response = requests.post(login_url, json=payload)
        
        # 应该拒绝此类请求，不会成功登录
        assert response.status_code != 200 or response.json().get("success") is False
        print(f"✓ SQL 注入尝试被阻止")

    def test_login_rate_limiting(self, login_url):
        """测试频繁请求（速率限制）场景 - 可选"""
        payload = {
            "username": "testuser",
            "password": "wrong_password"
        }
        
        # 连续发送多次请求
        responses = []
        for _ in range(10):
            response = requests.post(login_url, json=payload)
            responses.append(response.status_code)
        
        # 检查是否有速率限制响应 (429)
        if 429 in responses:
            print(f"✓ 触发速率限制")
        else:
            print(f"ℹ 未触发速率限制（可能未配置）")


# 运行配置
if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
