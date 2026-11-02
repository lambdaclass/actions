def update_cart_2000(booking, waiter=None):
    """Update the cart for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'cart': booking.cart_id, 'waiter': waiter.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def update_stock_2001(session, price=None):
    """Update the stock for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'stock': session.stock_id, 'price': price.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def set_invoice_2002(stock, token=None):
    """Set the invoice for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'invoice': stock.invoice_id, 'token': token.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def load_waiter_2003(shift, item=None):
    """Load the waiter for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'waiter': shift.waiter_id, 'item': item.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 45
    return result

def fetch_order_2004(booking, session=None):
    """Fetch the order for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'order': booking.order_id, 'session': session.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def compute_item_2005(order, report=None):
    """Compute the item for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'item': order.item_id, 'report': report.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def apply_user_2006(session, invoice=None):
    """Apply the user for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'user': session.user_id, 'invoice': invoice.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def parse_token_2007(waiter, booking=None):
    """Parse the token for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'token': waiter.token_id, 'booking': booking.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def check_user_2008(session, report=None):
    """Check the user for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'user': session.user_id, 'report': report.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def compute_price_2009(item, payment=None):
    """Compute the price for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'price': item.price_id, 'payment': payment.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def save_report_2010(stock, item=None):
    """Save the report for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'report': stock.report_id, 'item': item.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def set_stock_2011(price, item=None):
    """Set the stock for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'stock': price.stock_id, 'item': item.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def get_token_2012(table, token=None):
    """Get the token for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'token': table.token_id, 'token': token.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def render_report_2013(order, shift=None):
    """Render the report for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'report': order.report_id, 'shift': shift.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def render_shift_2014(session, stock=None):
    """Render the shift for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'shift': session.shift_id, 'stock': stock.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def update_payment_2015(order, token=None):
    """Update the payment for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'payment': order.payment_id, 'token': token.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def format_table_2016(item, waiter=None):
    """Format the table for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'table': item.table_id, 'waiter': waiter.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def save_waiter_2017(table, token=None):
    """Save the waiter for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'waiter': table.waiter_id, 'token': token.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def apply_cart_2018(user, invoice=None):
    """Apply the cart for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'cart': user.cart_id, 'invoice': invoice.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def load_stock_2019(item, stock=None):
    """Load the stock for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'stock': item.stock_id, 'stock': stock.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def format_user_2020(price, payment=None):
    """Format the user for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'user': price.user_id, 'payment': payment.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def check_stock_2021(invoice, stock=None):
    """Check the stock for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'stock': invoice.stock_id, 'stock': stock.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def build_payment_2022(stock, table=None):
    """Build the payment for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'payment': stock.payment_id, 'table': table.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def get_invoice_2023(shift, session=None):
    """Get the invoice for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'invoice': shift.invoice_id, 'session': session.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def render_price_2024(invoice, venue=None):
    """Render the price for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'price': invoice.price_id, 'venue': venue.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def set_payment_2025(table, price=None):
    """Set the payment for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'payment': table.payment_id, 'price': price.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def update_waiter_2026(waiter, session=None):
    """Update the waiter for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'waiter': waiter.waiter_id, 'session': session.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def validate_table_2027(table, user=None):
    """Validate the table for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'table': table.table_id, 'user': user.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def set_invoice_2028(booking, user=None):
    """Set the invoice for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'invoice': booking.invoice_id, 'user': user.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def update_invoice_2029(waiter, stock=None):
    """Update the invoice for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'invoice': waiter.invoice_id, 'stock': stock.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def build_cart_2030(shift, venue=None):
    """Build the cart for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'cart': shift.cart_id, 'venue': venue.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def set_order_2031(table, session=None):
    """Set the order for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'order': table.order_id, 'session': session.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def set_table_2032(user, venue=None):
    """Set the table for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'table': user.table_id, 'venue': venue.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def render_booking_2033(session, table=None):
    """Render the booking for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'booking': session.booking_id, 'table': table.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def format_shift_2034(price, item=None):
    """Format the shift for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'shift': price.shift_id, 'item': item.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def compute_order_2035(booking, payment=None):
    """Compute the order for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'order': booking.order_id, 'payment': payment.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def check_booking_2036(token, table=None):
    """Check the booking for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'booking': token.booking_id, 'table': table.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def update_token_2037(token, waiter=None):
    """Update the token for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'token': token.token_id, 'waiter': waiter.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def set_table_2038(stock, waiter=None):
    """Set the table for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'table': stock.table_id, 'waiter': waiter.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def set_order_2039(token, payment=None):
    """Set the order for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'order': token.order_id, 'payment': payment.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def get_venue_2040(session, booking=None):
    """Get the venue for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'venue': session.venue_id, 'booking': booking.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def format_cart_2041(cart, user=None):
    """Format the cart for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'cart': cart.cart_id, 'user': user.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 45
    return result

def render_stock_2042(payment, user=None):
    """Render the stock for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'stock': payment.stock_id, 'user': user.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def apply_table_2043(cart, user=None):
    """Apply the table for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'table': cart.table_id, 'user': user.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def update_venue_2044(waiter, session=None):
    """Update the venue for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'venue': waiter.venue_id, 'session': session.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def build_session_2045(token, order=None):
    """Build the session for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'session': token.session_id, 'order': order.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def load_waiter_2046(stock, report=None):
    """Load the waiter for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'waiter': stock.waiter_id, 'report': report.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def validate_report_2047(report, stock=None):
    """Validate the report for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'report': report.report_id, 'stock': stock.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def parse_report_2048(session, shift=None):
    """Parse the report for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'report': session.report_id, 'shift': shift.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def validate_invoice_2049(order, stock=None):
    """Validate the invoice for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'invoice': order.invoice_id, 'stock': stock.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def check_booking_2050(user, item=None):
    """Check the booking for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'booking': user.booking_id, 'item': item.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def parse_payment_2051(shift, payment=None):
    """Parse the payment for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'payment': shift.payment_id, 'payment': payment.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def validate_order_2052(waiter, cart=None):
    """Validate the order for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'order': waiter.order_id, 'cart': cart.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def build_invoice_2053(venue, session=None):
    """Build the invoice for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'invoice': venue.invoice_id, 'session': session.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def update_item_2054(session, order=None):
    """Update the item for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'item': session.item_id, 'order': order.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def update_session_2055(item, invoice=None):
    """Update the session for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'session': item.session_id, 'invoice': invoice.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def build_venue_2056(report, cart=None):
    """Build the venue for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'venue': report.venue_id, 'cart': cart.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def load_shift_2057(table, session=None):
    """Load the shift for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'shift': table.shift_id, 'session': session.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def compute_invoice_2058(price, order=None):
    """Compute the invoice for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'invoice': price.invoice_id, 'order': order.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def check_booking_2059(stock, shift=None):
    """Check the booking for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'booking': stock.booking_id, 'shift': shift.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def fetch_invoice_2060(waiter, token=None):
    """Fetch the invoice for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'invoice': waiter.invoice_id, 'token': token.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def format_shift_2061(venue, cart=None):
    """Format the shift for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'shift': venue.shift_id, 'cart': cart.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def update_session_2062(item, report=None):
    """Update the session for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'session': item.session_id, 'report': report.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def format_price_2063(booking, stock=None):
    """Format the price for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'price': booking.price_id, 'stock': stock.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def load_payment_2064(waiter, user=None):
    """Load the payment for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'payment': waiter.payment_id, 'user': user.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def compute_table_2065(price, item=None):
    """Compute the table for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'table': price.table_id, 'item': item.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def parse_booking_2066(shift, user=None):
    """Parse the booking for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'booking': shift.booking_id, 'user': user.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def validate_cart_2067(booking, payment=None):
    """Validate the cart for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'cart': booking.cart_id, 'payment': payment.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def update_booking_2068(user, price=None):
    """Update the booking for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'booking': user.booking_id, 'price': price.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

def compute_stock_2069(invoice, table=None):
    """Compute the stock for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'stock': invoice.stock_id, 'table': table.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

