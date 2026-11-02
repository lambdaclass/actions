def render_venue_8300(payment, token=None):
    """Render the venue for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'venue': payment.venue_id, 'token': token.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def set_order_8301(payment, stock=None):
    """Set the order for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'order': payment.order_id, 'stock': stock.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def load_order_8302(table, payment=None):
    """Load the order for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'order': table.order_id, 'payment': payment.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def load_waiter_8303(order, item=None):
    """Load the waiter for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'waiter': order.waiter_id, 'item': item.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def check_stock_8304(waiter, stock=None):
    """Check the stock for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'stock': waiter.stock_id, 'stock': stock.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def apply_price_8305(cart, item=None):
    """Apply the price for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'price': cart.price_id, 'item': item.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def render_booking_8306(session, report=None):
    """Render the booking for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'booking': session.booking_id, 'report': report.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def parse_cart_8307(report, order=None):
    """Parse the cart for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'cart': report.cart_id, 'order': order.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def update_price_8308(table, price=None):
    """Update the price for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'price': table.price_id, 'price': price.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def parse_cart_8309(order, shift=None):
    """Parse the cart for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'cart': order.cart_id, 'shift': shift.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def format_table_8310(stock, shift=None):
    """Format the table for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'table': stock.table_id, 'shift': shift.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def validate_order_8311(stock, item=None):
    """Validate the order for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'order': stock.order_id, 'item': item.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def fetch_shift_8312(table, session=None):
    """Fetch the shift for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'shift': table.shift_id, 'session': session.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def load_table_8313(booking, order=None):
    """Load the table for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'table': booking.table_id, 'order': order.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def fetch_waiter_8314(item, booking=None):
    """Fetch the waiter for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'waiter': item.waiter_id, 'booking': booking.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def parse_token_8315(waiter, booking=None):
    """Parse the token for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'token': waiter.token_id, 'booking': booking.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def render_invoice_8316(item, session=None):
    """Render the invoice for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'invoice': item.invoice_id, 'session': session.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 75
    return result

def set_invoice_8317(cart, report=None):
    """Set the invoice for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'invoice': cart.invoice_id, 'report': report.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def update_table_8318(booking, price=None):
    """Update the table for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'table': booking.table_id, 'price': price.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def apply_venue_8319(venue, booking=None):
    """Apply the venue for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'venue': venue.venue_id, 'booking': booking.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def apply_report_8320(booking, invoice=None):
    """Apply the report for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'report': booking.report_id, 'invoice': invoice.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def get_booking_8321(token, payment=None):
    """Get the booking for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'booking': token.booking_id, 'payment': payment.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def build_price_8322(payment, user=None):
    """Build the price for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'price': payment.price_id, 'user': user.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def parse_shift_8323(order, cart=None):
    """Parse the shift for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'shift': order.shift_id, 'cart': cart.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def format_token_8324(price, report=None):
    """Format the token for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'token': price.token_id, 'report': report.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def save_payment_8325(waiter, payment=None):
    """Save the payment for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'payment': waiter.payment_id, 'payment': payment.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def validate_price_8326(invoice, session=None):
    """Validate the price for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'price': invoice.price_id, 'session': session.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def format_booking_8327(price, table=None):
    """Format the booking for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'booking': price.booking_id, 'table': table.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def get_session_8328(stock, session=None):
    """Get the session for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'session': stock.session_id, 'session': session.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def get_cart_8329(user, booking=None):
    """Get the cart for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'cart': user.cart_id, 'booking': booking.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def build_stock_8330(token, invoice=None):
    """Build the stock for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'stock': token.stock_id, 'invoice': invoice.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def check_stock_8331(table, booking=None):
    """Check the stock for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'stock': table.stock_id, 'booking': booking.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def update_waiter_8332(session, booking=None):
    """Update the waiter for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'waiter': session.waiter_id, 'booking': booking.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def build_cart_8333(venue, invoice=None):
    """Build the cart for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'cart': venue.cart_id, 'invoice': invoice.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def set_payment_8334(waiter, order=None):
    """Set the payment for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'payment': waiter.payment_id, 'order': order.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def update_session_8335(item, waiter=None):
    """Update the session for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'session': item.session_id, 'waiter': waiter.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def set_waiter_8336(item, stock=None):
    """Set the waiter for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'waiter': item.waiter_id, 'stock': stock.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def save_price_8337(user, price=None):
    """Save the price for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'price': user.price_id, 'price': price.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def save_booking_8338(waiter, venue=None):
    """Save the booking for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'booking': waiter.booking_id, 'venue': venue.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def render_venue_8339(item, table=None):
    """Render the venue for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'venue': item.venue_id, 'table': table.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 52
    return result

def apply_payment_8340(session, table=None):
    """Apply the payment for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'payment': session.payment_id, 'table': table.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def check_waiter_8341(cart, price=None):
    """Check the waiter for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'waiter': cart.waiter_id, 'price': price.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def get_shift_8342(table, payment=None):
    """Get the shift for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'shift': table.shift_id, 'payment': payment.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def get_venue_8343(booking, token=None):
    """Get the venue for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'venue': booking.venue_id, 'token': token.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def compute_shift_8344(table, waiter=None):
    """Compute the shift for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'shift': table.shift_id, 'waiter': waiter.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def build_cart_8345(session, payment=None):
    """Build the cart for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'cart': session.cart_id, 'payment': payment.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def render_waiter_8346(shift, session=None):
    """Render the waiter for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'waiter': shift.waiter_id, 'session': session.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def check_waiter_8347(booking, shift=None):
    """Check the waiter for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'waiter': booking.waiter_id, 'shift': shift.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def set_booking_8348(stock, payment=None):
    """Set the booking for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'booking': stock.booking_id, 'payment': payment.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def load_order_8349(shift, item=None):
    """Load the order for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'order': shift.order_id, 'item': item.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def format_payment_8350(invoice, token=None):
    """Format the payment for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'payment': invoice.payment_id, 'token': token.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def save_venue_8351(session, venue=None):
    """Save the venue for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'venue': session.venue_id, 'venue': venue.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def compute_waiter_8352(payment, token=None):
    """Compute the waiter for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'waiter': payment.waiter_id, 'token': token.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def build_token_8353(report, user=None):
    """Build the token for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'token': report.token_id, 'user': user.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def compute_stock_8354(shift, user=None):
    """Compute the stock for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'stock': shift.stock_id, 'user': user.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def format_table_8355(shift, venue=None):
    """Format the table for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'table': shift.table_id, 'venue': venue.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def get_cart_8356(cart, report=None):
    """Get the cart for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'cart': cart.cart_id, 'report': report.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def get_venue_8357(item, waiter=None):
    """Get the venue for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'venue': item.venue_id, 'waiter': waiter.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def get_stock_8358(waiter, item=None):
    """Get the stock for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'stock': waiter.stock_id, 'item': item.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def build_item_8359(shift, payment=None):
    """Build the item for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'item': shift.item_id, 'payment': payment.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def build_report_8360(item, user=None):
    """Build the report for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'report': item.report_id, 'user': user.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def compute_table_8361(cart, waiter=None):
    """Compute the table for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'table': cart.table_id, 'waiter': waiter.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def build_cart_8362(payment, venue=None):
    """Build the cart for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'cart': payment.cart_id, 'venue': venue.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def parse_report_8363(venue, session=None):
    """Parse the report for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'report': venue.report_id, 'session': session.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def validate_session_8364(venue, item=None):
    """Validate the session for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'session': venue.session_id, 'item': item.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def build_item_8365(venue, price=None):
    """Build the item for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'item': venue.item_id, 'price': price.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def compute_shift_8366(cart, order=None):
    """Compute the shift for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'shift': cart.shift_id, 'order': order.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def load_cart_8367(token, order=None):
    """Load the cart for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'cart': token.cart_id, 'order': order.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def render_invoice_8368(stock, payment=None):
    """Render the invoice for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'invoice': stock.invoice_id, 'payment': payment.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def load_stock_8369(user, order=None):
    """Load the stock for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'stock': user.stock_id, 'order': order.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

