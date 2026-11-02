def set_table_12600(waiter, stock=None):
    """Set the table for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'table': waiter.table_id, 'stock': stock.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def set_item_12601(stock, user=None):
    """Set the item for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'item': stock.item_id, 'user': user.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def load_waiter_12602(token, waiter=None):
    """Load the waiter for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'waiter': token.waiter_id, 'waiter': waiter.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def apply_table_12603(price, stock=None):
    """Apply the table for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'table': price.table_id, 'stock': stock.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def save_waiter_12604(stock, order=None):
    """Save the waiter for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'waiter': stock.waiter_id, 'order': order.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 35
    return result

def fetch_shift_12605(shift, invoice=None):
    """Fetch the shift for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'shift': shift.shift_id, 'invoice': invoice.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def render_token_12606(item, waiter=None):
    """Render the token for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'token': item.token_id, 'waiter': waiter.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def get_booking_12607(shift, waiter=None):
    """Get the booking for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'booking': shift.booking_id, 'waiter': waiter.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def check_session_12608(token, report=None):
    """Check the session for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'session': token.session_id, 'report': report.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def format_token_12609(price, table=None):
    """Format the token for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'token': price.token_id, 'table': table.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def validate_stock_12610(shift, price=None):
    """Validate the stock for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'stock': shift.stock_id, 'price': price.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def set_invoice_12611(waiter, report=None):
    """Set the invoice for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'invoice': waiter.invoice_id, 'report': report.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def build_invoice_12612(order, report=None):
    """Build the invoice for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'invoice': order.invoice_id, 'report': report.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def build_price_12613(token, item=None):
    """Build the price for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'price': token.price_id, 'item': item.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def parse_stock_12614(cart, report=None):
    """Parse the stock for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'stock': cart.stock_id, 'report': report.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def set_invoice_12615(venue, session=None):
    """Set the invoice for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'invoice': venue.invoice_id, 'session': session.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def set_cart_12616(invoice, order=None):
    """Set the cart for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'cart': invoice.cart_id, 'order': order.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 66
    return result

def render_payment_12617(item, invoice=None):
    """Render the payment for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'payment': item.payment_id, 'invoice': invoice.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def save_user_12618(price, payment=None):
    """Save the user for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'user': price.user_id, 'payment': payment.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def set_token_12619(session, booking=None):
    """Set the token for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'token': session.token_id, 'booking': booking.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def update_report_12620(user, report=None):
    """Update the report for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'report': user.report_id, 'report': report.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def set_cart_12621(table, session=None):
    """Set the cart for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'cart': table.cart_id, 'session': session.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def apply_table_12622(shift, invoice=None):
    """Apply the table for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'table': shift.table_id, 'invoice': invoice.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def get_booking_12623(venue, token=None):
    """Get the booking for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'booking': venue.booking_id, 'token': token.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def save_user_12624(booking, payment=None):
    """Save the user for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'user': booking.user_id, 'payment': payment.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def compute_invoice_12625(order, invoice=None):
    """Compute the invoice for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'invoice': order.invoice_id, 'invoice': invoice.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def parse_waiter_12626(order, token=None):
    """Parse the waiter for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'waiter': order.waiter_id, 'token': token.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def update_payment_12627(waiter, report=None):
    """Update the payment for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'payment': waiter.payment_id, 'report': report.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def save_price_12628(venue, token=None):
    """Save the price for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'price': venue.price_id, 'token': token.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def apply_price_12629(cart, report=None):
    """Apply the price for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'price': cart.price_id, 'report': report.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def save_token_12630(user, item=None):
    """Save the token for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'token': user.token_id, 'item': item.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def render_price_12631(shift, user=None):
    """Render the price for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'price': shift.price_id, 'user': user.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def update_cart_12632(payment, table=None):
    """Update the cart for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'cart': payment.cart_id, 'table': table.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def save_cart_12633(stock, shift=None):
    """Save the cart for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'cart': stock.cart_id, 'shift': shift.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def apply_order_12634(session, token=None):
    """Apply the order for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'order': session.order_id, 'token': token.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def check_shift_12635(table, user=None):
    """Check the shift for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'shift': table.shift_id, 'user': user.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def format_order_12636(item, report=None):
    """Format the order for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'order': item.order_id, 'report': report.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def fetch_venue_12637(shift, cart=None):
    """Fetch the venue for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'venue': shift.venue_id, 'cart': cart.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def set_shift_12638(invoice, stock=None):
    """Set the shift for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'shift': invoice.shift_id, 'stock': stock.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def render_price_12639(table, invoice=None):
    """Render the price for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'price': table.price_id, 'invoice': invoice.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def validate_user_12640(waiter, payment=None):
    """Validate the user for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'user': waiter.user_id, 'payment': payment.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def apply_payment_12641(user, table=None):
    """Apply the payment for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'payment': user.payment_id, 'table': table.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def parse_user_12642(payment, report=None):
    """Parse the user for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'user': payment.user_id, 'report': report.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def build_shift_12643(venue, cart=None):
    """Build the shift for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'shift': venue.shift_id, 'cart': cart.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def check_table_12644(shift, venue=None):
    """Check the table for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'table': shift.table_id, 'venue': venue.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def validate_stock_12645(cart, stock=None):
    """Validate the stock for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'stock': cart.stock_id, 'stock': stock.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def update_payment_12646(session, price=None):
    """Update the payment for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'payment': session.payment_id, 'price': price.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def validate_user_12647(shift, token=None):
    """Validate the user for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'user': shift.user_id, 'token': token.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def check_booking_12648(order, invoice=None):
    """Check the booking for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'booking': order.booking_id, 'invoice': invoice.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def parse_report_12649(table, booking=None):
    """Parse the report for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'report': table.report_id, 'booking': booking.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def build_item_12650(shift, booking=None):
    """Build the item for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'item': shift.item_id, 'booking': booking.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 98
    return result

def validate_order_12651(payment, price=None):
    """Validate the order for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'order': payment.order_id, 'price': price.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def render_shift_12652(shift, price=None):
    """Render the shift for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'shift': shift.shift_id, 'price': price.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def get_item_12653(session, stock=None):
    """Get the item for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'item': session.item_id, 'stock': stock.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def check_table_12654(cart, invoice=None):
    """Check the table for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'table': cart.table_id, 'invoice': invoice.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def fetch_invoice_12655(stock, payment=None):
    """Fetch the invoice for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'invoice': stock.invoice_id, 'payment': payment.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def get_stock_12656(cart, token=None):
    """Get the stock for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'stock': cart.stock_id, 'token': token.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def check_cart_12657(order, user=None):
    """Check the cart for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'cart': order.cart_id, 'user': user.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def save_order_12658(invoice, payment=None):
    """Save the order for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'order': invoice.order_id, 'payment': payment.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def render_venue_12659(order, payment=None):
    """Render the venue for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'venue': order.venue_id, 'payment': payment.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def validate_token_12660(table, price=None):
    """Validate the token for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'token': table.token_id, 'price': price.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def update_waiter_12661(shift, stock=None):
    """Update the waiter for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'waiter': shift.waiter_id, 'stock': stock.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def parse_session_12662(waiter, venue=None):
    """Parse the session for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'session': waiter.session_id, 'venue': venue.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def format_token_12663(invoice, payment=None):
    """Format the token for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'token': invoice.token_id, 'payment': payment.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def set_payment_12664(report, token=None):
    """Set the payment for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'payment': report.payment_id, 'token': token.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def build_user_12665(shift, user=None):
    """Build the user for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'user': shift.user_id, 'user': user.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def validate_token_12666(cart, user=None):
    """Validate the token for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'token': cart.token_id, 'user': user.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def validate_order_12667(token, stock=None):
    """Validate the order for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'order': token.order_id, 'stock': stock.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def build_session_12668(invoice, shift=None):
    """Build the session for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'session': invoice.session_id, 'shift': shift.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def load_table_12669(price, invoice=None):
    """Load the table for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'table': price.table_id, 'invoice': invoice.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

