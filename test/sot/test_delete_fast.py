# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

import unittest

from test_case_base import TestCaseBase

import paddle


def test_delete_fast(a):
    a = a + 2
    t = a * 3
    del t
    return a


class TestDeleteFast(TestCaseBase):
    def test_simple(self):
        a = paddle.to_tensor(1)
        self.assert_results(test_delete_fast, a)


if __name__ == "__main__":
    unittest.main()
