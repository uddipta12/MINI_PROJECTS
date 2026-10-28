<%@ page contentType="text/html;charset=UTF-8" %>
<%@ taglib uri="jakarta.tags.core" prefix="c" %>
<!DOCTYPE html>
<html>
<head>
<title>Library Management</title>
<style>
  body { font-family: Arial; margin: 30px; background: #f4f6f8; }
  h1 { color: #2c3e50; }
  table { border-collapse: collapse; width: 100%; background: #fff; }
  th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
  th { background: #2c3e50; color: #fff; }
  .box { background: #fff; padding: 15px; margin-bottom: 20px; border-radius: 6px; }
  input { padding: 6px; margin-right: 6px; }
  button { padding: 6px 12px; cursor: pointer; }
  .AVAILABLE { color: green; font-weight: bold; }
  .ISSUED { color: red; font-weight: bold; }
</style>
</head>
<body>
<h1>Library Management System</h1>

<div class="box">
  <h3>Add Book</h3>
  <form method="post" action="books">
    <input type="hidden" name="action" value="add">
    <input name="title" placeholder="Title" required>
    <input name="author" placeholder="Author" required>
    <input name="isbn" placeholder="ISBN">
    <button>Add</button>
  </form>
</div>

<div class="box">
  <form method="get" action="books">
    <input name="q" placeholder="Search title or author" value="<c:out value='${param.q}'/>">
    <button>Search</button>
    <a href="books">Reset</a>
  </form>
</div>

<table>
  <tr>
    <th>ID</th><th>Title</th><th>Author</th><th>ISBN</th>
    <th>Status</th><th>Issued To</th><th>Actions</th>
  </tr>
  <c:forEach var="b" items="${books}">
    <tr>
      <td>${b.id}</td>
      <td><c:out value="${b.title}"/></td>
      <td><c:out value="${b.author}"/></td>
      <td><c:out value="${b.isbn}"/></td>
      <td class="${b.status}">${b.status}</td>
      <td><c:out value="${b.issuedTo}"/></td>
      <td>
        <c:if test="${b.status == 'AVAILABLE'}">
          <form method="post" action="books" style="display:inline">
            <input type="hidden" name="action" value="issue">
            <input type="hidden" name="id" value="${b.id}">
            <input name="name" placeholder="Student name" required>
            <button>Issue</button>
          </form>
        </c:if>
        <c:if test="${b.status == 'ISSUED'}">
          <a href="books?action=return&id=${b.id}">Return</a>
        </c:if>
        | <a href="books?action=delete&id=${b.id}"
             onclick="return confirm('Delete this book?')">Delete</a>
      </td>
    </tr>
  </c:forEach>
</table>
</body>
</html>