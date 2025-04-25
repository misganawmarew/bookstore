{
    'name': 'Bookstore Module',
    'version': '1.0',
    'category': 'Bookstore',
    'summary': 'Manage books, authors, and genres',
    'description': 'A module to manage bookstore operations, including book details, genres, authors, and automated archiving.',
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/book_details_view.xml',
        'views/genre_details_view.xml',
        'views/author_wizard_view.xml',
        'data/cron_job_data.xml',
    ],
    'demo': [
        'demo/demo_data.xml',
    ],
    'application': True,
}
