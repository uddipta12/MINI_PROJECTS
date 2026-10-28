package com.library.servlet;

import com.library.dao.BookDAO;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.SQLException;

@WebServlet("/books")
public class BookServlet extends HttpServlet {
    private final BookDAO dao = new BookDAO();

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {
        String action = req.getParameter("action");
        try {
            if ("delete".equals(action)) {
                dao.delete(Integer.parseInt(req.getParameter("id")));
                resp.sendRedirect("books");
                return;
            }
            if ("return".equals(action)) {
                dao.returnBook(Integer.parseInt(req.getParameter("id")));
                resp.sendRedirect("books");
                return;
            }
            req.setAttribute("books", dao.search(req.getParameter("q")));
            req.getRequestDispatcher("books.jsp").forward(req, resp);
        } catch (SQLException e) {
            throw new ServletException(e);
        }
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {
        req.setCharacterEncoding("UTF-8");
        String action = req.getParameter("action");
        try {
            if ("add".equals(action)) {
                dao.add(req.getParameter("title"),
                        req.getParameter("author"),
                        req.getParameter("isbn"));
            } else if ("issue".equals(action)) {
                dao.issue(Integer.parseInt(req.getParameter("id")),
                          req.getParameter("name"));
            }
            resp.sendRedirect("books");
        } catch (SQLException e) {
            throw new ServletException(e);
        }
    }
}