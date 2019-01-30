###**中文版地址https://q1mi.github.io/Django-REST-framework-documentation/tutorial/2-requests-and-responses_zh/**

#请求对象（Request objects）

REST框架引入了一个扩展了常规HttpRequest的Request对象，并提供了更灵活的请求解析。Request对象的核心功能是request.data属性，它与request.POST类似，但对于使用Web API更为有用。
```
request.POST  # 只处理表单数据  只适用于'POST'方法
request.data  # 处理任意数据  适用于'POST'，'PUT'和'PATCH'方法
```
#响应对象（Response objects）

REST框架还引入了一个Response对象，这是一种获取未渲染（unrendered）内容的TemplateResponse类型，并使用内容协商来确定返回给客户端的正确内容类型。
```
return Response(data)  # 渲染成客户端请求的内容类型。
```
#状态码（Status codes）

在你的视图（views）中使用纯数字的HTTP 状态码并不总是那么容易被理解。而且如果错误代码出错，很容易被忽略。REST框架为status模块中的每个状态代码（如HTTP_400_BAD_REQUEST）提供更明确的标识符。使用它们来代替纯数字的HTTP状态码是个很好的主意。

#包装（wrapping）API视图

REST框架提供了两个可用于编写API视图的包装器（wrappers）。

    用于基于函数视图的@api_view装饰器。
    用于基于类视图的APIView类。

这些包装器提供了一些功能，例如确保你在视图中接收到Request实例，并将上下文添加到Response，以便可以执行内容协商。

包装器还提供了诸如在适当时候返回405 Method Not Allowed响应，并处理在使用格式错误的输入来访问request.data时发生的任何ParseError异常。