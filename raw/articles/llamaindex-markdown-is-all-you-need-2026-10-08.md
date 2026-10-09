---
title: Markdown Is All You Need — selected source note
author: Murtaza Khomusi
publisher: LlamaIndex
source_type: article
source_url: https://www.llamaindex.ai/blog/markdown-is-all-you-need
published_at: 2026-10-08
captured_at: 2026-10-09
type: raw-source
status: raw
source_quality: partial
extraction_route: direct_html
capture_scope: selected-paraphrased-note
---

# Markdown Is All You Need — selected source note

## Provenance and capture scope

- 原文：[Markdown Is All You Need](https://www.llamaindex.ai/blog/markdown-is-all-you-need)，Murtaza Khomusi，LlamaIndex，2026-10-08；作者和日期来自文章页。
- 2026-10-09 直接读取原站可读正文，覆盖导言及 What Markdown preserves、Handling complex tables with HTML、Where JSON fits、Keeping images and layout information、Try it with LlamaParse 五节。
- 本文件是根据原文制作的选取式转述笔记，不是全文镜像，也不是把生成摘要作为原始证据。省略导航、营销页脚、装饰图片及完整代码块；`source_quality: partial` 描述本笔记的保存范围，原站正文已完整读取。
- 未读取正文链接指向的其他文档，未运行解析器或独立复现效果。原文是厂商的格式选择说明，没有独立对照实验、准确率或端到端成本数据。

## Selected source-backed points

### 文本正确不等于解析可靠

原文指出，PDF 中的文字和数值可以全部提取正确，但若失去所属章节或表格的关系，下游模型仍须猜测这些关系。文档搜索和抽取需要保留标题、阅读顺序、表格结构及元素周围的上下文，并让解析结果便于检查。

### Markdown 的职责

标题层级连接章节与小节；列表保留步骤及嵌套；简单表格给数值提供行列标签；链接保留引用。分块器可以按标题切分，并把章节标题带入切片。可读中间文本有助于区分解析、检索和生成阶段的问题。相比包含类型、样式和坐标的对象表示，Markdown 标记可能减少格式开销，但具体 Token 节省取决于文档和对照格式。

### 复杂表格示例及 HTML

文章用两年度营收与利润率、按区域分组的示例说明：转成普通管道表格后，年份跨列关系不再显式，第二层表头可能退化成数据行，区域分组依赖对空行的猜测。这里的财年与数值是说明性例子，不是实测财报数据。

简单结构可以通过展平字段名和增加区域列归一化；复杂结构可以在 Markdown 中嵌入 HTML，用 `colspan`、`rowspan` 和 `<thead>` 表达合并单元格及表头分组。HTML 只能表示解析器识别出的关系，不能保证这些关系识别正确。

### JSON、图片和坐标

JSON 可保存文档元素、元数据和供应用消费的抽取字段。Markdown 中间层便于人工检查并供多个提问或抽取 Schema 复用；直接从文档抽取也可以有效，不是所有任务都必须增加独立解析步骤。

图表可能需要数值及文字描述，空间关系图可能需要原图。页码与包围盒可关联解析内容，用于引用、高亮和视觉对齐；纯文本不是所有信息的替代品。

### 原文的检查方法

用熟悉的文档检查解析后的表格，确认数值仍对应正确的表头、单位和脚注，而不是只看输出整不整齐。

## Links retained from the article

- [LlamaParse table output documentation](https://developers.llamaindex.ai/llamaparse/parse/features/tables/)
- [LiteParse visual grounding example](https://www.llamaindex.ai/blog/liteparse-updates-september-2026)
- [LlamaParse application](https://cloud.llamaindex.ai/)

上述链接保留引用入口，不表示已核验其当前行为或建议采用该产品。
