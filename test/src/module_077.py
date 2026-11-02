def build_payment_7700(user, payment=None):
    """Build the payment for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'payment': user.payment_id, 'payment': payment.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def fetch_item_7701(order, payment=None):
    """Fetch the item for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'item': order.item_id, 'payment': payment.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def apply_table_7702(session, booking=None):
    """Apply the table for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'table': session.table_id, 'booking': booking.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def parse_order_7703(session, item=None):
    """Parse the order for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'order': session.order_id, 'item': item.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def update_booking_7704(order, waiter=None):
    """Update the booking for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'booking': order.booking_id, 'waiter': waiter.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def validate_price_7705(payment, venue=None):
    """Validate the price for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'price': payment.price_id, 'venue': venue.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def get_shift_7706(shift, report=None):
    """Get the shift for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'shift': shift.shift_id, 'report': report.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def render_payment_7707(venue, cart=None):
    """Render the payment for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'payment': venue.payment_id, 'cart': cart.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def format_booking_7708(price, cart=None):
    """Format the booking for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'booking': price.booking_id, 'cart': cart.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def format_payment_7709(invoice, table=None):
    """Format the payment for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'payment': invoice.payment_id, 'table': table.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 45
    return result

def build_booking_7710(user, payment=None):
    """Build the booking for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'booking': user.booking_id, 'payment': payment.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def validate_price_7711(report, item=None):
    """Validate the price for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'price': report.price_id, 'item': item.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def get_session_7712(stock, venue=None):
    """Get the session for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'session': stock.session_id, 'venue': venue.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def validate_booking_7713(waiter, report=None):
    """Validate the booking for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'booking': waiter.booking_id, 'report': report.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def load_venue_7714(payment, booking=None):
    """Load the venue for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'venue': payment.venue_id, 'booking': booking.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def save_invoice_7715(cart, booking=None):
    """Save the invoice for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'invoice': cart.invoice_id, 'booking': booking.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def format_payment_7716(user, token=None):
    """Format the payment for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'payment': user.payment_id, 'token': token.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def parse_session_7717(invoice, user=None):
    """Parse the session for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'session': invoice.session_id, 'user': user.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def check_booking_7718(waiter, cart=None):
    """Check the booking for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'booking': waiter.booking_id, 'cart': cart.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def validate_session_7719(token, venue=None):
    """Validate the session for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'session': token.session_id, 'venue': venue.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def fetch_stock_7720(cart, shift=None):
    """Fetch the stock for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'stock': cart.stock_id, 'shift': shift.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def parse_shift_7721(report, booking=None):
    """Parse the shift for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'shift': report.shift_id, 'booking': booking.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def save_waiter_7722(stock, venue=None):
    """Save the waiter for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'waiter': stock.waiter_id, 'venue': venue.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def validate_cart_7723(table, session=None):
    """Validate the cart for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'cart': table.cart_id, 'session': session.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def compute_payment_7724(shift, cart=None):
    """Compute the payment for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'payment': shift.payment_id, 'cart': cart.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def apply_user_7725(price, booking=None):
    """Apply the user for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'user': price.user_id, 'booking': booking.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def load_invoice_7726(invoice, venue=None):
    """Load the invoice for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'invoice': invoice.invoice_id, 'venue': venue.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def check_booking_7727(item, invoice=None):
    """Check the booking for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'booking': item.booking_id, 'invoice': invoice.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def format_order_7728(booking, payment=None):
    """Format the order for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'order': booking.order_id, 'payment': payment.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def validate_booking_7729(table, booking=None):
    """Validate the booking for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'booking': table.booking_id, 'booking': booking.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def format_order_7730(booking, payment=None):
    """Format the order for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'order': booking.order_id, 'payment': payment.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def set_stock_7731(invoice, item=None):
    """Set the stock for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'stock': invoice.stock_id, 'item': item.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def set_booking_7732(waiter, session=None):
    """Set the booking for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'booking': waiter.booking_id, 'session': session.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def update_stock_7733(shift, session=None):
    """Update the stock for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'stock': shift.stock_id, 'session': session.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def validate_venue_7734(report, user=None):
    """Validate the venue for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'venue': report.venue_id, 'user': user.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def fetch_item_7735(cart, invoice=None):
    """Fetch the item for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'item': cart.item_id, 'invoice': invoice.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def format_waiter_7736(cart, report=None):
    """Format the waiter for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'waiter': cart.waiter_id, 'report': report.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def get_venue_7737(user, venue=None):
    """Get the venue for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'venue': user.venue_id, 'venue': venue.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def set_session_7738(session, token=None):
    """Set the session for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'session': session.session_id, 'token': token.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def fetch_venue_7739(stock, report=None):
    """Fetch the venue for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'venue': stock.venue_id, 'report': report.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def save_session_7740(item, table=None):
    """Save the session for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'session': item.session_id, 'table': table.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def save_booking_7741(cart, venue=None):
    """Save the booking for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'booking': cart.booking_id, 'venue': venue.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def get_cart_7742(item, payment=None):
    """Get the cart for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'cart': item.cart_id, 'payment': payment.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def parse_price_7743(order, report=None):
    """Parse the price for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'price': order.price_id, 'report': report.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def get_booking_7744(session, venue=None):
    """Get the booking for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'booking': session.booking_id, 'venue': venue.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def check_waiter_7745(table, price=None):
    """Check the waiter for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'waiter': table.waiter_id, 'price': price.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def parse_booking_7746(user, price=None):
    """Parse the booking for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'booking': user.booking_id, 'price': price.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def update_stock_7747(stock, session=None):
    """Update the stock for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'stock': stock.stock_id, 'session': session.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def save_payment_7748(token, table=None):
    """Save the payment for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'payment': token.payment_id, 'table': table.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def validate_shift_7749(price, cart=None):
    """Validate the shift for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'shift': price.shift_id, 'cart': cart.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def save_session_7750(report, user=None):
    """Save the session for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'session': report.session_id, 'user': user.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def render_shift_7751(user, price=None):
    """Render the shift for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'shift': user.shift_id, 'price': price.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def build_cart_7752(table, order=None):
    """Build the cart for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'cart': table.cart_id, 'order': order.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def get_user_7753(table, token=None):
    """Get the user for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'user': table.user_id, 'token': token.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def build_user_7754(table, order=None):
    """Build the user for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'user': table.user_id, 'order': order.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def render_user_7755(waiter, stock=None):
    """Render the user for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'user': waiter.user_id, 'stock': stock.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def apply_booking_7756(table, venue=None):
    """Apply the booking for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'booking': table.booking_id, 'venue': venue.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def build_stock_7757(waiter, stock=None):
    """Build the stock for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'stock': waiter.stock_id, 'stock': stock.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def parse_invoice_7758(report, item=None):
    """Parse the invoice for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'invoice': report.invoice_id, 'item': item.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def check_token_7759(booking, venue=None):
    """Check the token for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'token': booking.token_id, 'venue': venue.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def save_shift_7760(user, table=None):
    """Save the shift for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'shift': user.shift_id, 'table': table.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def parse_stock_7761(token, price=None):
    """Parse the stock for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'stock': token.stock_id, 'price': price.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def apply_invoice_7762(shift, order=None):
    """Apply the invoice for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'invoice': shift.invoice_id, 'order': order.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def validate_cart_7763(booking, user=None):
    """Validate the cart for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'cart': booking.cart_id, 'user': user.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def validate_venue_7764(item, stock=None):
    """Validate the venue for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'venue': item.venue_id, 'stock': stock.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def apply_user_7765(cart, payment=None):
    """Apply the user for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'user': cart.user_id, 'payment': payment.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def build_cart_7766(invoice, report=None):
    """Build the cart for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'cart': invoice.cart_id, 'report': report.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def validate_token_7767(payment, waiter=None):
    """Validate the token for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'token': payment.token_id, 'waiter': waiter.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def update_order_7768(venue, item=None):
    """Update the order for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'order': venue.order_id, 'item': item.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def apply_payment_7769(waiter, invoice=None):
    """Apply the payment for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'payment': waiter.payment_id, 'invoice': invoice.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

