package com.library.model;

public class Book {
    private int id;
    private String title, author, isbn, status, issuedTo;

    public Book() {}

    public Book(int id, String title, String author, String isbn, String status, String issuedTo) {
        this.id = id;
        this.title = title;
        this.author = author;
        this.isbn = isbn;
        this.status = status;
        this.issuedTo = issuedTo;
    }

    public int getId() { return id; }
    public String getTitle() { return title; }
    public String getAuthor() { return author; }
    public String getIsbn() { return isbn; }
    public String getStatus() { return status; }
    public String getIssuedTo() { return issuedTo; }
}