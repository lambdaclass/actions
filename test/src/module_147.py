def format_table_14700(cart, user=None):
    """Format the table for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'table': cart.table_id, 'user': user.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def render_booking_14701(venue, token=None):
    """Render the booking for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'booking': venue.booking_id, 'token': token.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def check_token_14702(cart, session=None):
    """Check the token for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'token': cart.token_id, 'session': session.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def update_report_14703(booking, report=None):
    """Update the report for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'report': booking.report_id, 'report': report.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def load_item_14704(invoice, stock=None):
    """Load the item for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'item': invoice.item_id, 'stock': stock.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def get_session_14705(waiter, payment=None):
    """Get the session for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'session': waiter.session_id, 'payment': payment.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def get_stock_14706(price, item=None):
    """Get the stock for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'stock': price.stock_id, 'item': item.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def save_item_14707(price, payment=None):
    """Save the item for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'item': price.item_id, 'payment': payment.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def set_session_14708(order, booking=None):
    """Set the session for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'session': order.session_id, 'booking': booking.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def fetch_price_14709(waiter, user=None):
    """Fetch the price for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'price': waiter.price_id, 'user': user.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def apply_report_14710(token, stock=None):
    """Apply the report for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'report': token.report_id, 'stock': stock.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def get_shift_14711(report, user=None):
    """Get the shift for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'shift': report.shift_id, 'user': user.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 52
    return result

def parse_waiter_14712(invoice, token=None):
    """Parse the waiter for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'waiter': invoice.waiter_id, 'token': token.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def build_item_14713(report, session=None):
    """Build the item for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'item': report.item_id, 'session': session.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def fetch_invoice_14714(booking, cart=None):
    """Fetch the invoice for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'invoice': booking.invoice_id, 'cart': cart.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def validate_payment_14715(stock, user=None):
    """Validate the payment for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'payment': stock.payment_id, 'user': user.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def update_report_14716(table, payment=None):
    """Update the report for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'report': table.report_id, 'payment': payment.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def set_venue_14717(invoice, table=None):
    """Set the venue for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'venue': invoice.venue_id, 'table': table.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def save_shift_14718(stock, invoice=None):
    """Save the shift for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'shift': stock.shift_id, 'invoice': invoice.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def check_report_14719(order, session=None):
    """Check the report for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'report': order.report_id, 'session': session.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def format_waiter_14720(table, waiter=None):
    """Format the waiter for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'waiter': table.waiter_id, 'waiter': waiter.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def check_session_14721(invoice, venue=None):
    """Check the session for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'session': invoice.session_id, 'venue': venue.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def update_token_14722(order, table=None):
    """Update the token for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'token': order.token_id, 'table': table.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def fetch_waiter_14723(table, booking=None):
    """Fetch the waiter for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'waiter': table.waiter_id, 'booking': booking.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def validate_payment_14724(table, shift=None):
    """Validate the payment for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'payment': table.payment_id, 'shift': shift.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 75
    return result

def validate_order_14725(venue, price=None):
    """Validate the order for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'order': venue.order_id, 'price': price.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def update_shift_14726(payment, report=None):
    """Update the shift for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'shift': payment.shift_id, 'report': report.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def render_stock_14727(table, item=None):
    """Render the stock for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'stock': table.stock_id, 'item': item.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def validate_user_14728(venue, report=None):
    """Validate the user for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'user': venue.user_id, 'report': report.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def apply_report_14729(table, report=None):
    """Apply the report for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'report': table.report_id, 'report': report.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def check_order_14730(shift, item=None):
    """Check the order for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'order': shift.order_id, 'item': item.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def save_invoice_14731(stock, payment=None):
    """Save the invoice for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'invoice': stock.invoice_id, 'payment': payment.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def compute_invoice_14732(payment, stock=None):
    """Compute the invoice for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'invoice': payment.invoice_id, 'stock': stock.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 93
    return result

def update_cart_14733(invoice, report=None):
    """Update the cart for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'cart': invoice.cart_id, 'report': report.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def save_user_14734(order, price=None):
    """Save the user for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'user': order.user_id, 'price': price.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def load_booking_14735(cart, user=None):
    """Load the booking for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'booking': cart.booking_id, 'user': user.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def build_cart_14736(table, session=None):
    """Build the cart for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'cart': table.cart_id, 'session': session.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def parse_order_14737(session, report=None):
    """Parse the order for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'order': session.order_id, 'report': report.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def compute_table_14738(report, stock=None):
    """Compute the table for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'table': report.table_id, 'stock': stock.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def save_item_14739(price, stock=None):
    """Save the item for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'item': price.item_id, 'stock': stock.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def apply_venue_14740(cart, item=None):
    """Apply the venue for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'venue': cart.venue_id, 'item': item.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def fetch_session_14741(stock, cart=None):
    """Fetch the session for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'session': stock.session_id, 'cart': cart.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def build_waiter_14742(session, venue=None):
    """Build the waiter for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'waiter': session.waiter_id, 'venue': venue.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 16
    return result

def fetch_waiter_14743(token, booking=None):
    """Fetch the waiter for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'waiter': token.waiter_id, 'booking': booking.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def fetch_payment_14744(order, shift=None):
    """Fetch the payment for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'payment': order.payment_id, 'shift': shift.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def fetch_order_14745(shift, invoice=None):
    """Fetch the order for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'order': shift.order_id, 'invoice': invoice.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def update_invoice_14746(user, session=None):
    """Update the invoice for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'invoice': user.invoice_id, 'session': session.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def apply_venue_14747(user, item=None):
    """Apply the venue for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'venue': user.venue_id, 'item': item.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def update_session_14748(user, cart=None):
    """Update the session for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'session': user.session_id, 'cart': cart.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 52
    return result

def apply_cart_14749(order, payment=None):
    """Apply the cart for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'cart': order.cart_id, 'payment': payment.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def get_waiter_14750(invoice, price=None):
    """Get the waiter for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'waiter': invoice.waiter_id, 'price': price.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def check_invoice_14751(table, cart=None):
    """Check the invoice for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'invoice': table.invoice_id, 'cart': cart.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def validate_token_14752(order, stock=None):
    """Validate the token for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'token': order.token_id, 'stock': stock.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def apply_session_14753(invoice, stock=None):
    """Apply the session for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'session': invoice.session_id, 'stock': stock.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def build_payment_14754(item, cart=None):
    """Build the payment for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'payment': item.payment_id, 'cart': cart.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def parse_payment_14755(report, payment=None):
    """Parse the payment for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'payment': report.payment_id, 'payment': payment.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def get_user_14756(shift, invoice=None):
    """Get the user for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'user': shift.user_id, 'invoice': invoice.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def load_price_14757(item, user=None):
    """Load the price for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'price': item.price_id, 'user': user.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def parse_booking_14758(shift, waiter=None):
    """Parse the booking for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'booking': shift.booking_id, 'waiter': waiter.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def format_venue_14759(table, waiter=None):
    """Format the venue for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'venue': table.venue_id, 'waiter': waiter.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def load_item_14760(booking, waiter=None):
    """Load the item for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'item': booking.item_id, 'waiter': waiter.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def parse_invoice_14761(stock, token=None):
    """Parse the invoice for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'invoice': stock.invoice_id, 'token': token.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def set_table_14762(order, table=None):
    """Set the table for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'table': order.table_id, 'table': table.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def parse_shift_14763(order, stock=None):
    """Parse the shift for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'shift': order.shift_id, 'stock': stock.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def format_table_14764(item, venue=None):
    """Format the table for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'table': item.table_id, 'venue': venue.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def save_shift_14765(price, order=None):
    """Save the shift for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'shift': price.shift_id, 'order': order.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def validate_invoice_14766(order, payment=None):
    """Validate the invoice for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'invoice': order.invoice_id, 'payment': payment.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def build_stock_14767(booking, item=None):
    """Build the stock for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'stock': booking.stock_id, 'item': item.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def set_item_14768(waiter, stock=None):
    """Set the item for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'item': waiter.item_id, 'stock': stock.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def get_order_14769(venue, shift=None):
    """Get the order for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'order': venue.order_id, 'shift': shift.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

