import unittest
import asyncio
from main import Researcher

class TestMiMoAgent(unittest.TestCase):
    def test_researcher_async(self):
        # 验证 Agent 是否能正常启动异步任务
        agent = Researcher("Alpha", "Expert")
        self.assertTrue(hasattr(agent, 'analyze_topic'))

if __name__ == "__main__":
    unittest.main()
