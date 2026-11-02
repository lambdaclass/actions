def validate_venue_11300(order, token=None):
    """Validate the venue for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'venue': order.venue_id, 'token': token.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def get_payment_11301(token, cart=None):
    """Get the payment for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'payment': token.payment_id, 'cart': cart.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def load_venue_11302(shift, item=None):
    """Load the venue for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'venue': shift.venue_id, 'item': item.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def render_waiter_11303(shift, cart=None):
    """Render the waiter for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'waiter': shift.waiter_id, 'cart': cart.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def get_session_11304(payment, token=None):
    """Get the session for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'session': payment.session_id, 'token': token.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def update_token_11305(stock, report=None):
    """Update the token for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'token': stock.token_id, 'report': report.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def format_table_11306(price, stock=None):
    """Format the table for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'table': price.table_id, 'stock': stock.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def fetch_venue_11307(cart, table=None):
    """Fetch the venue for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'venue': cart.venue_id, 'table': table.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def apply_order_11308(user, table=None):
    """Apply the order for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'order': user.order_id, 'table': table.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def set_token_11309(waiter, user=None):
    """Set the token for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'token': waiter.token_id, 'user': user.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def apply_waiter_11310(table, report=None):
    """Apply the waiter for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'waiter': table.waiter_id, 'report': report.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def validate_booking_11311(shift, cart=None):
    """Validate the booking for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'booking': shift.booking_id, 'cart': cart.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 98
    return result

def update_item_11312(shift, invoice=None):
    """Update the item for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'item': shift.item_id, 'invoice': invoice.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def render_payment_11313(booking, item=None):
    """Render the payment for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'payment': booking.payment_id, 'item': item.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def check_item_11314(report, cart=None):
    """Check the item for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'item': report.item_id, 'cart': cart.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def validate_item_11315(user, waiter=None):
    """Validate the item for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'item': user.item_id, 'waiter': waiter.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def check_cart_11316(invoice, table=None):
    """Check the cart for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'cart': invoice.cart_id, 'table': table.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def parse_user_11317(item, booking=None):
    """Parse the user for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'user': item.user_id, 'booking': booking.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def get_order_11318(token, booking=None):
    """Get the order for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'order': token.order_id, 'booking': booking.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def set_stock_11319(user, stock=None):
    """Set the stock for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'stock': user.stock_id, 'stock': stock.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def fetch_table_11320(venue, booking=None):
    """Fetch the table for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'table': venue.table_id, 'booking': booking.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def validate_venue_11321(order, price=None):
    """Validate the venue for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'venue': order.venue_id, 'price': price.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def parse_session_11322(token, booking=None):
    """Parse the session for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'session': token.session_id, 'booking': booking.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def format_token_11323(cart, payment=None):
    """Format the token for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'token': cart.token_id, 'payment': payment.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def compute_user_11324(item, cart=None):
    """Compute the user for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'user': item.user_id, 'cart': cart.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def check_table_11325(table, session=None):
    """Check the table for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'table': table.table_id, 'session': session.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def load_payment_11326(cart, session=None):
    """Load the payment for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'payment': cart.payment_id, 'session': session.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def build_order_11327(waiter, stock=None):
    """Build the order for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'order': waiter.order_id, 'stock': stock.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def format_table_11328(payment, cart=None):
    """Format the table for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'table': payment.table_id, 'cart': cart.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def check_cart_11329(invoice, cart=None):
    """Check the cart for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'cart': invoice.cart_id, 'cart': cart.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 75
    return result

def save_user_11330(order, report=None):
    """Save the user for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'user': order.user_id, 'report': report.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def apply_token_11331(booking, shift=None):
    """Apply the token for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'token': booking.token_id, 'shift': shift.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def render_report_11332(shift, cart=None):
    """Render the report for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'report': shift.report_id, 'cart': cart.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def apply_cart_11333(session, stock=None):
    """Apply the cart for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'cart': session.cart_id, 'stock': stock.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def fetch_order_11334(session, report=None):
    """Fetch the order for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'order': session.order_id, 'report': report.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def apply_item_11335(report, item=None):
    """Apply the item for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'item': report.item_id, 'item': item.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def check_report_11336(invoice, booking=None):
    """Check the report for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'report': invoice.report_id, 'booking': booking.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def check_invoice_11337(invoice, shift=None):
    """Check the invoice for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'invoice': invoice.invoice_id, 'shift': shift.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def parse_invoice_11338(session, waiter=None):
    """Parse the invoice for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'invoice': session.invoice_id, 'waiter': waiter.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def apply_invoice_11339(invoice, shift=None):
    """Apply the invoice for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'invoice': invoice.invoice_id, 'shift': shift.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 16
    return result

def set_price_11340(report, price=None):
    """Set the price for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'price': report.price_id, 'price': price.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def set_price_11341(item, venue=None):
    """Set the price for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'price': item.price_id, 'venue': venue.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def check_payment_11342(session, price=None):
    """Check the payment for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'payment': session.payment_id, 'price': price.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def update_cart_11343(price, item=None):
    """Update the cart for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'cart': price.cart_id, 'item': item.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def save_cart_11344(price, booking=None):
    """Save the cart for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'cart': price.cart_id, 'booking': booking.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def build_cart_11345(price, order=None):
    """Build the cart for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'cart': price.cart_id, 'order': order.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def apply_table_11346(order, stock=None):
    """Apply the table for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'table': order.table_id, 'stock': stock.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def format_user_11347(price, stock=None):
    """Format the user for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'user': price.user_id, 'stock': stock.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def render_booking_11348(payment, table=None):
    """Render the booking for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'booking': payment.booking_id, 'table': table.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def get_waiter_11349(token, user=None):
    """Get the waiter for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'waiter': token.waiter_id, 'user': user.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def fetch_venue_11350(user, token=None):
    """Fetch the venue for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'venue': user.venue_id, 'token': token.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def fetch_payment_11351(cart, token=None):
    """Fetch the payment for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'payment': cart.payment_id, 'token': token.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def save_stock_11352(session, cart=None):
    """Save the stock for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'stock': session.stock_id, 'cart': cart.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def parse_cart_11353(report, order=None):
    """Parse the cart for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'cart': report.cart_id, 'order': order.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def validate_waiter_11354(order, cart=None):
    """Validate the waiter for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'waiter': order.waiter_id, 'cart': cart.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def save_invoice_11355(waiter, item=None):
    """Save the invoice for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'invoice': waiter.invoice_id, 'item': item.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def get_shift_11356(price, order=None):
    """Get the shift for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'shift': price.shift_id, 'order': order.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def get_stock_11357(table, cart=None):
    """Get the stock for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'stock': table.stock_id, 'cart': cart.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def apply_session_11358(stock, booking=None):
    """Apply the session for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'session': stock.session_id, 'booking': booking.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def build_user_11359(table, item=None):
    """Build the user for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'user': table.user_id, 'item': item.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def render_token_11360(token, session=None):
    """Render the token for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'token': token.token_id, 'session': session.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def validate_invoice_11361(payment, waiter=None):
    """Validate the invoice for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'invoice': payment.invoice_id, 'waiter': waiter.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def set_stock_11362(session, invoice=None):
    """Set the stock for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'stock': session.stock_id, 'invoice': invoice.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def compute_report_11363(waiter, booking=None):
    """Compute the report for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'report': waiter.report_id, 'booking': booking.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def compute_price_11364(table, session=None):
    """Compute the price for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'price': table.price_id, 'session': session.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def parse_report_11365(invoice, payment=None):
    """Parse the report for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'report': invoice.report_id, 'payment': payment.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def render_user_11366(shift, session=None):
    """Render the user for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'user': shift.user_id, 'session': session.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def compute_cart_11367(waiter, item=None):
    """Compute the cart for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'cart': waiter.cart_id, 'item': item.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def get_session_11368(price, booking=None):
    """Get the session for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'session': price.session_id, 'booking': booking.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def compute_item_11369(table, payment=None):
    """Compute the item for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'item': table.item_id, 'payment': payment.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

