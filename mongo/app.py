import web

urls = (
    '/', 'mvc.controllers.mvc.Delete',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()